import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
import numpy as np

countryData, entireData, dict_data=[],[],{}

t_ignore='        \t\n'
###DEFINING TOKENS###
tokens = ('BEGINTABLE',
'OPENTABLE', 'OPENHEAD','CLOSEHEAD','CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF','SPACE',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')

###############Tokenizer Rules################
def t_BEGINTABLE(t):
     r'<table.id="main_table_countries_yesterday"[^>]*>'
     return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t

def t_OPENHEAD(t):
    r'<thead[^>]*>'
    return t

def t_CLOSEHEAD(t):
    r'<\thead[^>]*>'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t

def t_SPACE(t):
    r'&\#160;'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9+,.\/\u00E9 ]+'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'

def t_CLOSEDIV(t):
    r'</div[^>]*>'

def t_OPENSTYLE(t):
    r'<style[^>]*>'
    return t

def t_CLOSESTYLE(t):
    r'</style[^>]*>'
    return t

def t_OPENSPAN(t):
    r'<span[^>]*>'

def t_CLOSESPAN(t):
    r'</span[^>]*>'

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_table(p):
    '''table : BEGINTABLE skiptag OPENHEAD content skiprow CLOSEHEADER OPENTABLE skiprows handlerow'''
           
def p_skiprows(p):
    '''skiprows : skiprow skiprow skiprow skiprow skiprow skiprow skiprow'''
    #print("skiprows completed")

#skip the entire <th> tag
def p_skiprow(p):
    '''skiprow : OPENROW unwanted CLOSEROW'''
    #print("skip row ")

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | SPACE skiptag
               | empty'''

def p_unwanted(p):
    '''unwanted : GARBAGE unwanted
                | OPENHREF unwanted
                | CLOSEHREF unwanted
                | CONTENT unwanted
                | OPENDATA unwanted
                | CLOSEDATA unwanted
                | SPACE unwanted
                | OPENSPAN unwanted
                | CLOSESPAN unwanted
                | OPENHEADER unwanted
                | CLOSEHEADER unwanted
                | empty'''

# handle the <tr> tag
def p_handlerow(p):
    '''handlerow : OPENROW dataCell CLOSEROW  handlerow
                 | empty'''

#used to extract contect from table cell
def p_dataCell(p):
    '''dataCell : OPENDATA CONTENT CLOSEDATA dataCell
                | OPENDATA OPENHREF content CLOSEHREF CLOSEDATA dataCell
                | OPENDATA CLOSEDATA dataCell
                | empty'''

    global countryData
    if len(p)==2:
        global entireData
        if len(countryData)!=0: entireData.append(countryData[:])
        countryData.clear()
    elif len(p)==4: countryData.append(' ')
    elif len(p)==5: countryData.append(p[2])
    else:
        ind1,ind2 = p[2].find('href="'), p[2].find('">')
        url = p[2][ind1+6:ind2]
        if url.find('country')!=-1: countryData.append(url)
        countryData.append(p[3])
   
def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : CONTENT content
               | empty'''
    if len(p)==3:
        p[0]=p[1]+p[2]
    else:
        p[0]=''
    
def p_error(p):
    pass

#Parses the given Data
def parse(data):
    tokens_file = open('tokens.txt','w',encoding="utf-8")
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        tokens_file.write(str(tok)+"\n")
    parser = yacc.yacc()
    parser.parse(data)

# downloads web page for given url and stores them in given file_name
def downloadWebPage(url, file_name):
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open(file_name,'w',encoding="utf-8")
    f.write(mydata)
    f.close


def extractData():
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    file_obj.close()
    parse(data)

def extract_4_cases(dict_data):
    while(True):
        ip=input("Enter country name(-1 for exit): ")
        if(ip=="-1"): break
        data = dict_data[ip.lower()]
        new, daily,recovered,active = data[4],data[6],data[8],data[9]
        print(f'Active Cases: {active}\nDaily Deaths: {daily}\nNew Recovered: {recovered}\nNew Cases:{new}')

#########DRIVER FUNCTION#######
def main():
    downloadWebPage('https://www.worldometers.info/coronavirus/','webpage.html')
    print("Extracting")
    extractData()
    countries = []
    country_file = open('worldometers_countrylist.txt','r')
    file = open('data1.txt','w')
    arr=['Country Name','Url','Total cases','Active Cases', 'Total Deaths', 'Totat Recovered', 'Total Tests', 'Deaths/million'', Tests/million', 'New Cases', 'New Death', 'New Recovery']
    ind=[1,2,3,9,5,7,13,12,14,4,6,8]
    for x in country_file.readlines(): countries.append(x.replace('\n',''))
    file = open('data1.txt','w')
    file.write(('\t'.join(arr))+'\n')
    for i in entireData:
        i.reverse()
        for j in range(2,len(i)): 
            i[j]=i[j].replace(',','').replace(' ','')
            if i[j]=='': i[j]= '0'
        if (i[1].lower()=='world'): 
            dict_data[str(i[1]).lower()]=['','world','']+i[2:]
            data = ['','world','']+i[2:]
        else: 
            dict_data[str(i[1]).lower()]=i[:]
            data=i[:]
        if (str(i[1])in countries):
            val=[]
            for x in ind:val.append(data[x])
            string = '\t'.join(val)
            file.write(string+'\n')
    file.close()

    file = open('data.txt','w')
    for i in entireData:
        string = ','.join(i[0:14])
        file.write(string+'\n')
    file.close()

    file = open('gloabl_countries_data.txt','w')
    string = '\t'.join(arr)
    file.write(string+'\n')
    #extract_4_cases(dict_data)

if __name__ == '__main__':
    main()