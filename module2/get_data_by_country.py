import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  
import os 

###DEFINING TOKENS###
tokens = ('BEGINTABLE','H6SPAN','H5SPAN', 'H3SPAN','H2SPAN','CONTENT','GARBAGE','ENDTABLE')

t_ignore = ' \t\n'

dic = {}

global file_pointer
file_pointer = None
#____________###Tokenizer Rules________________
def t_BEGINTABLE(t):
    r'<h1.id="firstHeading".class="firstHeading.mw-first-heading'
    return t

def t_ENDTABLE(t):
     r'<span.class="mw-headline".id="See_also">'
     return t

def t_H2SPAN(t):
    r'<h2><span.class="mw-headline"<[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9 \,\.\–]+'
    return t

def t_H5SPAN(t):
    r'<h5.class="mw-headline" id="Symptoms-of-COVID-19">Symptoms of COVID-19</h5>'
    return t

def t_H6SPAN(t):
    r'<h6.class="mw-headline" id="Disproportionate-impact-on-certan-populations">Disproportionate impact on certain populations</h6>'
    return t
def t_H3SPAN(t):
    r'<span.class="mw-headline".id="<[^>]*>'
    return t




def t_GARBAGE(t):
    r"(<[^>]*> | /\[[a-z0-9A-Z]*] | &nbsp; | edit | &\#160;)"
    t.lexer.skip(0)


def t_error(t):
    t.lexer.skip(1)
#____________________________________________________________________________________________________________________________________________________________________________________________________
#                                          #GRAMMAR RULES
def p_start(p):
    '''start : table'''
    p[0] = p[1]


def p_dealh6span(p):
    ''' dealh6span : H6SPAN CONTENT content dealh5span empty
                    | content CONTENT dealh4span CONTENT dealh5span H5SPAN content CONTENT dealh6span 
                    | content CONTENT dealh5span content H6SPAN content CONTENT dealh6span 
                    | empty'''
    if(len(p)==8):
        file_pointer.write(f"____{p[2]}____\n")
        file_pointer.write(f"____{p[3]}____\n")
    if(len(p)==12):
        file_pointer.write(f"____{p[2]}____\n")
    
def p_skiptag(p):
    '''skiptag : content skiptag
               | GARBAGE skiptag
               | H2SPAN skiptag
               | H3SPAN skiptag
               | H5SPAN Skiptag
               | H6SPAN skiptag
               | empty 

      '''

def p_dealh5span(p):
    
    ''' dealh5span : H5SPAN CONTENT content 
                    | H5SPAN content CONTENT dealh4span CONTENT CONTENT dealh6span CONTENT
                    | content CONTENT dealh4span H6SPAN CONTENT CONTENT dealh6span CONTENT
                    | content CONTENT H5SPAN CONTENT CONTENT dealh6span CONTENT
                    | empty'''
    if(len(p)==5):
        file_pointer.write(f"____{p[2]}____\n")
        file_pointer.write(f"____{p[3]}____\n")

    if(len(p)==11):
        file_pointer.write(f"____{p[2]}____\n")



def p_dealh2span(p):
    '''dealh2span : H2SPAN CONTENT content dealh5span
                    | H2SPAN content CONTENT dealh4span CONTENT dealh5span content CONTENT dealh6span 
                    | H2SPAN content 
                    | H2SPAN CONTENT dealh4span content CONTENT 
                '''
    if(len(p)==5):
        file_pointer.write(f"____{p[2]}____\n")
        file_pointer.write(f"____{p[3]}____\n")
    if(len(p)==3):

        file_pointer.write(f"____{p[2]}____\n")
    if len(p)==7:
        file_pointer.write(f"____{p[5]}____\n")
        

def p_dealh4span(p):
    '''dealh4span : H3SPAN CONTENT content
                | H3SPAN CONTENT dealdata content CONTENT dealh4span
                | H3SPAN CONTENT dealh5span CONTENT empty content
                | H3SPAN empty CONTENT dealh2span'''
    
    # print(f"____{p[2]}____")
    # print(p[3])
    if len(p)==4:
        global file_pointer
        file_pointer.write(p[2]+"\n")
        file_pointer.write(p[3]+"\n")
    if len(p)==7:
        global file_pointer
        file_pointer.write(p[2]+"\n")
        file_pointer.write(p[4]+"\n")      

def p_dealdata(p):
    '''dealdata : dealh2span dealh4span 
                | dealh2span 
                | dealh4span
                | dealh5span
                | dealh6span dealh5span
                | dealh6span
                        
    '''
    file_pointer.write("\n")
    

def p_dealhead(p):
    '''dealhead :  dealdata dealhead
                | empty
    '''

def p_table(p):
    '''table : skiptag  BEGINTABLE content dealhead ENDTABLE skiptag'''

 
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
 
#__________#DRIVER FUNCTION____###
def main(link,path1):
    print(link)
    global file_pointer
    file_pointer = open(path1+".txt","w")
    webpage_file(link)
    fetch_data()
    file_pointer.close()
