import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  
import os

import info_response_2020


tokens = ('BEGINTABLE','H6SPAN','H5SPAN','H4SPAN','H3SPAN', 'OPENPARA','CLOSEPARA','OPENHEAD','CLOSEHEAD','CONTENT','GARBAGE','ENDTABLE')

t_ignore = ' \t\n'

lis = []


file_pointer = open("2019.txt","w")

def t_BEGINTABLE(t):
    r'<span.class="mw-headline".id="Unconfirmed_reports_of_early_cases">Unconfirmed.reports.of.early.cases</span>'
    return t
def t_OPENPARA(t):
    r'<p[^>]*>'
    return t
 
def t_CLOSEPARA(t):
    r'</p>'
    return t


def t_ENDTABLE(t):
     r'<span.class="mw-headline".id="See_also">See.also'
     return t


def t_GARBAGE(t):
    r"(<[^>]*> | &nbsp; | &\#160;)"
    t.lexer.skip(0)

def t_CONTENT(t):
    r'[A-Za-z0-9 \,\.\–\/]+'
    return t

def t_OPENHEAD(t):
    r'<h2[^>]*>'
    return t
 
def t_CLOSEHEAD(t):
    r'</h2>'
    return t
def t_H6SPAN(t):
    r'<h6 class="mw-headline" id="Disproportionate-impact-on-certan-populations">Disproportionate impact on certain populations</h6>'
    return t
def t_H3SPAN(t):
    r'<h3 class="mw-headline" id="Disevaluate-populations">certain populations</h3>'
    return t

def t_H4SPAN(t):
    r'<h4><span class="mw-headline" id="TIMELINE-H4">COVID DETAILS </span></h4>'
    return t


def t_H5SPAN(t):
    r'<h5 class="mw-headline" id="Symptoms-of-COVID-19">Symptoms of COVID-19</h5>'
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
               | OPENPARA skiptag
               | CLOSEPARA skiptag
               | OPENHEAD skiptag
               | CLOSEHEAD skiptag
               | empty 

      '''

def p_skipper(p):
    '''skipper : content skipper
               | GARBAGE skipper
               | OPENPARA skipper
               | CLOSEPARA skipper
               | CLOSEHEAD skipper
               | empty 

      '''
def p_dealh3span(p):
    '''dealh3span : H3SPAN CONTENT content dealh6span
                    | H3SPAN CONTENT dealh5span content empty empty
                    | H3SPAN CONTENT dealh6span content empty empty content'''
    
    global filep
    if len(p)==5:
        filep.write(f"....{p[2]}....\n")
        filep.write(f"{p[3]}\n")
def checker(s):
    if s is not None:
        return True
    return False
def p_printpara(p):
    '''printpara : OPENPARA dealh5span content H6SPAN CLOSEPARA
                | OPENPARA CONTENT dealh6span H5SPAN CLOSEPARA
                | OPENPARA content CLOSEPARA
                | OPENPARA CONTENT dealh5span content CLOSEPARA
                | OPENPARA CONTENT OPENHEAD content CLOSEPARA'''
    # print(p[2])
    if len(p)==4: 
        file_pointer.write(f"{p[2]}\n")
    elif len(p)==7:
        file_pointer.write(f"{p[4]}\n")
    
def p_dealpara(p):
    '''dealpara :  printpara dealpara
                | printhead empty dealhead printpara dealpara
                | printhead empty dealh6span H5SPAN dealhead printpara dealpara

    '''
    if(len(p)==3):
        p[0]=p[1]
    if len(p)==8:
        print(p[4])

def p_printhead(p):
    '''printhead : OPENHEAD content CLOSEHEAD'''
    if checker(p[2]) or p[2] !="" or (p[2]):
        file_pointer.write(f"_____{p[2]}_____\n")

def p_dealhead(p):
    '''dealhead : printhead content printpara dealhead
                  | printpara dealhead
                  | CONTENT dealhead printpara empty
                  | content printpara dealhead
                  | OPENHEAD ENDTABLE skiptag
                  |
    '''
    if(len(p)== 6):
        # print(f"{p[4]}\n")
        file_pointer.write(f"{p[4]}\n")
    elif(len(p)==4):
        # print(f"{p[2]}\n")
        file_pointer.write(str(p[2])+"\n")
    # print(len(p))
def p_dealh5span(p):
    ''' dealh5span : H5SPAN CONTENT content 
                    | H5SPAN content CONTENT dealh4span CONTENT CONTENT dealh6span CONTENT
                    | dealh6span CONTENT skipper H5SPAN content
                    | dealh6span CONTENT skiptag H6SPAN CONTENT dealh5span
                    | empty'''
    if(len(p)==5):
        file_pointer.write(f"....{p[2]}....\n")
        file_pointer.write(f"....{p[3]}....\n")
    if(len(p)==11):
        file_pointer.write(f"....{p[2]}....\n")



def p_table(p):
    '''table : skiptag  BEGINTABLE skipper  dealhead '''

 
def p_empty(p):
    '''empty :'''
    pass
 
def p_content(p):
    '''content : CONTENT content
               | empty'''
    if(len(p)==3):
        if(p[1]!="edit"):  
            p[0] = str(p[1])+str(p[2])
        else:
            p[0] = ""
        
    
 
def p_error(p):
    pass

def webpage_file(url):
    print("webpage processing")
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
 
#########DRIVER FUNCTION#######
def main(link):
    webpage_file(link)
    fetch_data()

if __name__ == '__main__':
    with open("responselinks.txt", "r") as fp1:
        data = fp1.read()
        base = "https://en.wikipedia.org"
        for link in data.split("\n"):
            attr = link.strip('">').split(" ")
            if attr[-1] in ["2020", "2021", "2022"]:
                print(base+attr[1].split("=")[1].strip('"'))
                info_response_2020.main(base + attr[1].split("=")[1].strip('"'), f"response_{attr[-1]}", attr[-2])
