import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  
import os
import info_year_2023
import info_year_2020




###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'H6SPAN','H5SPAN','H4SPAN','H3SPAN','OPENPARA','CLOSEPARA','OPENHEAD','CLOSEHEAD','CONTENT','GARBAGE','ENDTABLE')

t_ignore = ' \t\n'
# lis to store all the values
lis = []


filepointer = open("2019.txt","w")
###############Tokenizer Rules################
def t_BEGINTABLE(t):
    r'<span.class="mw-headline".id="Unconfirmed_reports_of_early_cases">Unconfirmed.reports.of.early.cases</span>'
    return t

def t_ENDTABLE(t):
     r'<span.class="mw-headline".id="See_also">See.also'
     return t
def t_OPENPARA(t):
    r'<p[^>]*>'
    return t
 
def t_CLOSEPARA(t):
    r'</p>'
    return t

def t_OPENHEAD(t):
    r'<h2[^>]*>'
    return t
 
def t_CLOSEHEAD(t):
    r'</h2>'
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
def t_H3SPAN(t):
    r'<h3 class="mw-headline" id="Disevaluate-populations">certain populations</h3>'
    return t



def t_GARBAGE(t):
    r"(<[^>]*> | &nbsp; | &\#160;)"
    # print(t.value,len(t.value))
    t.lexer.skip(0)

def t_CONTENT(t):
    r'[A-Za-z0-9 \,\.\–\/]+'
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
def p_handleh3span(p):
    '''handleh3span : H3SPAN CONTENT content handleh6span
                    | H3SPAN CONTENT handleh5span content empty empty
                    | H3SPAN CONTENT handleh6span content empty empty content'''
    
    # print(f"____p[2]+"____")
    
    global filep
    if len(p)==5:
        filep.write("____"+p[2]+"____\n")
        filep.write(f"{p[3]}\n")

def p_skipper(p):
    '''skipper : content skipper
               | GARBAGE skipper
               | OPENPARA skipper
               | CLOSEPARA skipper
               | CLOSEHEAD skipper
               | empty 

      '''
def p_handleh5span(p):
    ''' handleh5span : H5SPAN CONTENT content 
                    | H5SPAN content CONTENT handleh4span CONTENT CONTENT handleh6span CONTENT
                    | handleh6span CONTENT skipper H5SPAN content
                    | handleh6span CONTENT skiptag H6SPAN CONTENT handleh5span
                    | empty'''
            # print("____"+p[2]+"____")
    if(len(p)==5):
        filepointer.write("____"+p[2]+"____\n")
        filepointer.write("____"+p[3]+"____\n")
        # print(p[2])
        # print(p[3])
    if(len(p)==11):
        filepointer.write("____"+p[2]+"____\n")
    # global filepointerointer
def p_handleh4span(p):
    '''handleh4span : H4SPAN CONTENT content handleh3span handleh5span empty handleh6span
                    | H4SPAN CONTENT content handleh5span H6SPAN 
                    | H4SPAN CONTENT content handleh5span H3SPAN CONTENT empty empty content
                    '''
    
    # print("____"+p[2]+"____")
    if len(p)==8:
        print(p[3])
        global filep
        filep.write(p[2]+"\n")
        filep.write(p[3]+"\n")

def p_handleh6span(p):
    
    ''' handleh6span : H6SPAN CONTENT content handleh5span empty
                    | H6SPAN content CONTENT handleh4span CONTENT handleh5span content CONTENT handleh6span 
                    | H6SPAN content CONTENT handleh5span CONTENT handleh6span content CONTENT handleh6span 
                    | empty'''
        # print("____"+p[2]+"____")
    if(len(p)==7):
        filepointer.write("____"+p[2]+"____\n")
        filepointer.write("____"+p[3]+"____\n")
        # print(p[2])
        # print(p[3])
    if(len(p)==11):
        filepointer.write("____"+p[2]+"____\n")

def p_printpara(p):
    '''printpara : OPENPARA content CLOSEPARA'''
    # print(p[2])
    filepointer.write(f"{p[2]}\n")
    
def p_handlepara(p):
    '''handlepara :  printpara handlepara
                |

    '''
    if(len(p)==3):
        p[0]=p[1]

def p_printhead(p):
    '''printhead : OPENHEAD content CLOSEHEAD
                | OPENHEAD handleh5span CONTENT printpara content handleh6span CLOSEHEAD 
                | empty'''
    if len(p)==4:
        if(p[2]):
            # print(f"____p[2]+____")
            filepointer.write("____p[2]+____\n")
    if len(p)==6:
        if(p[3]):
            # print(f"____p[2]+"____")
            filepointer.write("____"+p[3]+"____\n")

def p_handlehead(p):
    '''handlehead : printhead handleh5span content printpara handleh6span handlehead
                  | printpara handlehead
                  | handleh6span CONTENT handleh5span H5SPAN printhead 
                  | content handleh5span printpara handlehead
                  | OPENHEAD ENDTABLE handleh6span skiptag empty empty
                  | 
    '''
    if(len(p)== 8):
        filepointer.write(f"{p[3]}\n")
    elif(len(p)==5):
        filepointer.write(str(p[3])+"\n")
    # print(len(p))



def p_table(p):
    '''table : skiptag  BEGINTABLE skipper  handlehead '''

 
def p_empty(p):
    '''empty :'''
    pass
 
def p_content(p):
    '''content : CONTENT content
               | empty'''
    if(len(p)==3):
        if(p[1]!="edit"):
            p[0] = "{}{}".format(p[1], p[2])        
        else:
            p[0] = ""
        
    
 
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
 
#########DRIVER FUNCTION#######
def main(link):
    webpage_file(link)
    fetch_data()

if __name__ == '__main__':

    with open("timelinelinks.txt", "r") as fp1:
        data = fp1.read()
        base = "https://en.wikipedia.org"
        # link='<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_2023" title="Timeline of the COVID-19 pandemic in 2023">'
        # link=link.strip('">')
        # attr = link.split(" ")
        # print(attr)
        # url=base+attr[1].split("=")[1].strip('"')
        links = [link.strip('">') for link in data.split("\n")]
        for link in links:
            attr = link.split(" ")
            url=base+attr[1].split("=")[1].strip('"')
            print(attr[-1])
            if(attr[-1]=="2019"):
                main(url)
            elif attr[-1] in ["2023", "2024"]:
                info_year_year = attr[-1]
                info_year_2023.main(url, info_year_year)
            elif attr[-1] in ["2020", "2021", "2022"]:
                info_year_year = attr[-1]
                info_year_2020.main(url, info_year_year, attr[-2])