import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  
import os
 
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'H3SPAN','H4SPAN', 'H5SPAN', 'H6SPAN',
'CONTENT','GARBAGE','ENDTABLE')
 
t_ignore = ' \t\n'
 
# lis to store all the values
dic = {}
 
global file_pointer
file_pointer = None
# file_pointer = open(path+"2023.txt","w")
###############Tokenizer Rules################
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
    r'<h5 class="mw-headline" id="Symptoms-of-COVID-19">Symptoms of COVID-19</h5>'
    return t
 

def t_H6SPAN(t):
    r'<h6 class="mw-headline" id="Disproportionate-impact-on-certan-populations">Disproportionate impact on certain populations</h6>'
    return t
 
# def t_OPENUL(t):
#     r'<ul>'
#     return t
# def t_CLOSEUL(t):
#     r'</ul>'
#     return t
 
def t_GARBAGE(t):
    r"(<[^>]*> | /\[[a-z0-9A-Z]*] | &nbsp; | &\#160;| edit)"
    # print(t.value,len(t.value))
    t.lexer.skip(0)
 
def t_CONTENT(t):
    r'[A-Za-z0-9 \,\.]+'
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
               | H4SPAN skiptag
               | H3SPAN skiptag
               | empty
 
      '''
 
# def p_dealh5span(p):    
#     ''' dealh5span : H5SPAN CONTENT content
#                     | H5SPAN content CONTENT dealh4span CONTENT CONTENT dealh3span CONTENT
#                     | H5SPAN content CONTENT dealh4span CONTENT CONTENT deal CONTENT
#                     | content CONTENT dealh4span CONTENT CONTENT H6SPAN content CONTENT dealh5span
#                     | empty'''
    
#     global file_pointer
#     if(len(p)==5):
#         file_pointer.write(f"____{p[2]}____\n")
#         file_pointer.write(f"____{p[3]}____\n")
#     if(len(p)==11):
#         file_pointer.write(f"____{p[2]}____\n")

 
def p_dealh3span(p):
    '''dealh3span : H3SPAN CONTENT content
                | H3SPAN CONTENT dealh5span CONTENT empty content H6SPAN empty empty
                | H3SPAN CONTENT dealh6span CONTENT content dealh6span H5SPAN empty empty empty
                | H3SPAN CONTENT dealh6span CONTENT content dealh6span H5SPAN empty empty dealh6span empty'''
   
    global file_pointer
    if len(p)==4:
        if(file_pointer):
            file_pointer.close()
        global path
        file_pointer = open(path+f"{p[2]}.txt","w")


# def p_dealh7span(p):
#     '''dealh7span : H4SPAN CONTENT content
#                 | CONTENT  CONTENT empty content H6SPAN empty empty empty empty
#                 | H4SPAN CONTENT CONTENT content  H5SPAN empty empty empty'''
#     global file_pointer
#     if len(p)==4:
#         file_pointer.write(p[2]+"\n")
#         file_pointer.write(p[3]+"\n")
#     elif len(p)==11:
#         file_pointer.write(p[2]+"\n")
#         file_pointer.write(p[4]+"\n")
 
def p_dealh4span(p):
    '''dealh4span : H4SPAN CONTENT content
                | H4SPAN CONTENT dealh5span CONTENT empty content H6SPAN empty empty
                | H4SPAN CONTENT dealh6span CONTENT content dealh6span H5SPAN empty empty empty'''
    global file_pointer
    if len(p)==4:
        file_pointer.write(p[2]+"\n")
        file_pointer.write(p[3]+"\n")
    elif len(p)==11:
        file_pointer.write(p[2]+"\n")
        file_pointer.write(p[4]+"\n")


def p_dealh7span(p):
    '''dealh7span : H4SPAN CONTENT content
                | CONTENT  CONTENT empty content H6SPAN empty empty empty empty
                | H4SPAN CONTENT CONTENT content  H5SPAN empty empty empty'''
    global file_pointer
    if len(p)==4:
        file_pointer.write(p[2]+"\n")
        file_pointer.write(p[3]+"\n")
    elif len(p)==11:
        file_pointer.write(p[2]+"\n")
        file_pointer.write(p[4]+"\n")
    

def p_dealdata(p):
    '''dealdata : dealh3span dealh4span
                | dealh4span
                       
    '''
    # print()
    file_pointer.write("\n")
   


def p_dealh5span(p):    
    ''' dealh5span : H5SPAN CONTENT content
                    | H5SPAN content CONTENT dealh4span CONTENT CONTENT dealh6span CONTENT
                    | content CONTENT dealh4span CONTENT CONTENT H6SPAN CONTENT
                    | content CONTENT dealh4span CONTENT CONTENT H6SPAN content CONTENT dealh5span
                    | empty'''
    if(len(p)==5):
        file_pointer.write(f"____{p[2]}____\n")
        file_pointer.write(f"____{p[3]}____\n")
    if(len(p)==11):
        file_pointer.write(f"____{p[2]}____\n")

   
def p_dealh6span(p):
   
    ''' dealh6span : H6SPAN CONTENT content dealh5span empty
                    | H6SPAN CONTENT content dealh5span content CONTENT dealh6span
                    | content CONTENT dealh5span CONTENT H5SPAN content CONTENT H6SPAN
                    | content CONTENT dealh5span CONTENT H6SPAN content CONTENT dealh6span
                    | empty'''
    if(len(p)==8):
        file_pointer.write(f"____{p[2]}____\n")
        file_pointer.write(f"____{p[3]}____\n")
    if(len(p)==12):
        file_pointer.write(f"____{p[2]}____\n")
 

def p_dealhead(p):
    '''dealhead :  dealdata dealhead 
                  |
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
        p[0] = str(p[1])+str(p[2])
    else:
       
        p[0]=""
   
 
def p_error(p):
    # print("\n\n\n\n\nerror....",p)
    pass
 
#########DRIVER FUNCTION#######
def main(link,path1):
   
    # Check if the directory already exists
    if not os.path.exists(path1):
        # If not, create the directory
        os.makedirs(path1)
    global path
    path = path1+"/"
    req = Request(link,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('webpage.html','w',encoding="utf-8")
    f.write(mydata)
    f.close
 
    print("fetching data.... Please wait....")
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    fp = open("lextokens.txt","w")
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        try:
            fp.write(str(tok)+"\n")
        except:
            pass
    fp.close()
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
 
 