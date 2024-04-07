import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  
import os 


###DEFINING TOKENS###
tokens = ('BEGINTABLE','H6SPAN','H5SPAN','H4SPAN','H3SPAN','H2SPAN','CONTENT','GARBAGE','ENDTABLE')
t_ignore = ' \t\n'

dic = {}
###############Tokenizer Rules################
def t_BEGINTABLE(t):
    r'<h1.id="firstHeading"[^>]*>'
    return t
def t_ENDTABLE(t):
     r'<span.class="mw-headline".id="See_also">'
     return t

def t_H2SPAN(t):
    r'<h2><span.class="mw-headline"[^>]*>'
    return t


def t_H3SPAN(t):
    r'<span.class="mw-headline".id="[^>]*>'
    return t

def t_H4SPAN(t):
    r'<h4><span class="mw-headline" id="TIMELINE-H4">COVID DETAILS </span></h4>'
    return t


def t_H5SPAN(t):
    r'<h5 class="mw-headline" id="Symptoms-of-COVID-19">Symptoms of COVID-19</h5>'
    return t

def t_H6SPAN(t):
    r'<h6 class="mw-headline" id="Disproportionate-impact-on-certan-populations">Disproportionate impact on certain populations</h6>'
    return t



def t_GARBAGE(t):
    r"(<[^>]*> | /\[[a-z0-9A-Z]*] | &nbsp; | &\#160;| edit)"
    t.lexer.skip(0)

def t_CONTENT(t):
    r'[A-Za-z0-9 \,\.\–]+'
    return t



def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
                                            #GRAMMAR RULES
def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_skiptag(p):
    '''skiptag : content skiptag
               | GARBAGE skiptag
               | H2SPAN skiptag
               | H3SPAN skiptag
               | H4SPAN skiptag
               | H5SPAN skiptag
               | H6SPAN skiptag
               | empty 

      '''
def p_handleh5span(p):
    
    ''' handleh5span : H5SPAN CONTENT content 
                    | H5SPAN content CONTENT handleh4span CONTENT CONTENT handleh6span CONTENT                    
                    | empty'''

    if(len(p)==5):
        filepointer.write("____"+str(p[2])+"____\n")
        filepointer.write("____"+str(p[2])+"____\n")
        # print(p[2])
        # print(p[3])
    if(len(p)==11):
        filepointer.write("____"+str(p[2])+"____\n")
    # global filepointer

def p_handleh6span(p):
    #'''handleh4span : H3SPAN CONTENT content'''
    
    ''' handleh6span : H6SPAN CONTENT content handleh5span empty
                    | H6SPAN content CONTENT handleh4span CONTENT handleh5span content CONTENT handleh6span 
                    | H6SPAN content CONTENT handleh5span CONTENT handleh6span content CONTENT handleh6span 
                    | empty'''
        # print(f"____{p[2]}____")
    if(len(p)==7):
        filepointer.write("____"+str(p[2])+"____\n")
        filepointer.write("____"+str(p[2])+"____\n")
        # print(p[2])
        # print(p[3])
    if(len(p)==11):
        filepointer.write("____"+str(p[2])+"____\n")
    # global filepointer
                    

def p_handleh2span(p):
    '''handleh2span : H2SPAN CONTENT content 
                    | H2SPAN content
                '''
    
    # print(f"____{p[2]}____")
    if(len(p)==4):
        filepointer.write("____"+str(p[2])+"____\n")
        filepointer.write("____"+str(p[3])+"____\n")
        # print(p[2])
        # print(p[3])
    if(len(p)==3):
        filepointer.write("____"+str(p[2])+"____\n")
    # global filepointer
   
  
    # filepointer = open(path+f"{p[2]}.txt","w")

def p_handleh4span(p):
    '''handleh4span : H3SPAN CONTENT content
                    | H3SPAN handleh6span CONTENT content H5SPAN handleh5span'''
    
    # print(f"____{p[2]}____")
    # print(p[3])
    if len(p)==4:
        global filepointer
        filepointer.write(p[2]+"\n")
        filepointer.write(p[3]+"\n")

def p_handledata(p):
    '''handledata : handleh2span handleh4span handleh6span
                | handleh2span 
                | handleh4span
                | handleh6span
                | handleh5span
                        
    '''
    # print()
    filepointer.write("\n")
    

def p_handlehead(p):
    '''handlehead :  handledata handlehead 
                |
    '''
    



def p_table(p):
    '''table : skiptag  BEGINTABLE content handlehead handleh6span ENDTABLE skiptag'''

 
def p_empty(p):
    '''empty :'''
    pass
 
def p_content(p):
    '''content : CONTENT content
               | empty'''
    if(len(p)==3):
        p[0] = str(p[1])+str(p[2])
    else:
       
        p[0]=""
    
 
def p_error(p):
    pass
 

def webpage_file(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage_data = urlopen(req).read()
    page_data = webpage_data.decode("utf8")
    with open('webpage.html', 'w', encoding="utf-8") as f:
        f.write(page_data)
def fetch_data():
    html_file = open('webpage.html', 'r', encoding="utf-8")
    html_data = html_file.read()
    print("Fetching data")
    token_file = open("lextokens.txt", "w")
    lexer = lex.lex()
    lexer.input(html_data)
    for token in lexer:
        try:
            token_file.write(str(token) + "\n")
        except:
            pass
    token_file.close()
    parser = yacc.yacc()
    parser.parse(html_data)
    html_file.close()
 

def main(link,path1,month):
    if not os.path.exists(path1):
        os.makedirs(path1)
    global path
    path = path1+"/"

    global filepointer
   
    
    filepointer = open(path+f"{month}.txt","w")
    
    webpage_file(link)
    fetch_data()
    filepointer.close()

