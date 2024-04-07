import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  
import os 


###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'H3SPAN','H4SPAN','H6SPAN','H5SPAN','CONTENT','GARBAGE','ENDTABLE')
t_ignore = ' \t\n'

dic = {}
def t_BEGINTABLE(t):
    r'<span.class="mw-headline".id="Pandemic_chronology">Pandemic.chronology</span>'
    return t

def t_ENDTABLE(t):
     r'<span.class="mw-headline".id="Summary"'
     return t
def t_H3SPAN(t):
    r'<h3><span.class="mw-headline[^>]*>'
    return t

def t_H4SPAN(t):
    r'<h4><span.class="mw-headline[^>]*>'
    return t

def t_H5SPAN(t):
    r'<h5><span.class="mw-headline" id="Symptoms-of-COVID-19">Symptoms of COVID-19</h5>'
    return t

def t_H6SPAN(t):
    r'<h6><span.class="mw-headline" id="Disproportionate-impact-on-certan-populations">Disproportionate impact on certain populations</h6>'
    return t

def t_GARBAGE(t):
    r"(<[^>]*> | /\[[a-z0-9A-Z]*] | &nbsp; | &\#160;| edit)"
    t.lexer.skip(0)

def t_CONTENT(t):
    r'[A-Za-z0-9 \,\.]+'
    return t



def t_error(t):
    t.lexer.skip(1)

def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_dealh4span(p):
    '''dealh4span : H4SPAN CONTENT content dealh3span dealh5span empty dealh6span
                    | H4SPAN CONTENT content dealh5span H6SPAN 
                    | H4SPAN CONTENT content dealh5span H3SPAN CONTENT empty empty content
                    '''
    

    if len(p)==8:
        print(p[3])
        global filep
        filep.write(p[2]+"\n")
        filep.write(p[3]+"\n")



def p_dealh6span(p):
    ''' dealh6span : H6SPAN CONTENT content empty
                    | content CONTENT dealh4span CONTENT dealh5span H5SPAN content CONTENT dealh6span 
                    | H6SPAN content CONTENT dealh5span CONTENT dealh6span content CONTENT dealh6span 
                    | content CONTENT dealh5span CONTENT dealh4span CONTENT H6SPAN content dealh6span
                    | empty'''

    global filep
    if(len(p)==8):
        filep.write(f"____{p[2]}____\n")
        filep.write(f"____{p[3]}____\n")
    if(len(p)==12):
        filep.write(f"____{p[2]}____\n")

    

def p_dealh3span(p):
    '''dealh3span : H3SPAN CONTENT content dealh6span
                    | H3SPAN CONTENT dealh5span content empty empty 
                    | H3SPAN CONTENT dealh6span content empty empty dealh5span'''

    
    global filep
    if len(p)==5:
        filep.write("____"+str({p[2]})+"____\n")
        filep.write(f"{p[3]}\n")
    elif len(p)==7:
        filep.write("____"+str(p[2])+"____\n")
        filep.write(f"{p[4]}\n")
    elif len(p)==8:
        filep.write(f"____{p[2]}____\n")
        filep.write(f"{p[4]}\n")

def p_skiptag(p):
    '''skiptag : content skiptag
               | GARBAGE skiptag
               | H4SPAN skiptag
               | H3SPAN skiptag
               | H5SPAN skiptag
               | H6SPAN skiptag
               | empty 

      '''

def p_table(p):
    '''table : skiptag  BEGINTABLE  dealhead ENDTABLE skiptag'''

 
def p_empty(p):
    '''empty :'''
    pass
 
def p_content(p):
    '''content : CONTENT content
               | empty'''
    if(len(p)==3):
        p[0] = "{}{}".format(p[1], p[2])    
    else:
       
        p[0]=""
        
        
def p_dealhead(p):
    '''dealhead :  dealh3span dealhead
                  | empty
    '''
    
def p_dealh5span(p):
    ''' dealh5span : H5SPAN CONTENT content 
                    | H5SPAN content CONTENT dealh4span CONTENT CONTENT dealh6span CONTENT
                    | content CONTENT dealh4span H6SPAN CONTENT CONTENT dealh6span CONTENT
                    | content CONTENT dealh4span CONTENT H6SPAN CONTENT skiptag CONTENT dealh6span CONTENT
                    | empty'''

    global filep
    if(len(p)==5):
        filep.write(f"____{p[2]}____\n")
        filep.write(f"____{p[3]}____\n")
    if(len(p)==11):
        filep.write(f"____{p[2]}____\n")
 
def p_error(p):

    pass
 


def webpage_file(url):
    print("Webpage processing")
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage_data = urlopen(req).read()
    page_data = webpage_data.decode("utf8")
    with open('webpage.html', 'w', encoding="utf-8") as f:
        f.write(page_data)
def fetch_data():
    global filep
    print("Fetching the Data")
    web_obj= open('webpage.html','r',encoding="utf-8")
    data=web_obj.read()
    fp = open("lextokens.txt","w")
    lexer = lex.lex()
    lexer.input(data)
    for i in lexer:
        try:
            fp.write(str(i)+"\n")
        except:
            pass
    fp.close()
    parser_obj = yacc.yacc()
    parser_obj.parse(data)
    web_obj.close()

    filep.close()
    
    
def main(link,path1,month):
    print(link,path1,month)
    if not os.path.exists(path1):
        os.makedirs(path1)
    global path
    path = path1+"/"

    global filep
    filep = open(path+f"{month}.txt","w")
   
    webpage_file(link)
    fetch_data()
