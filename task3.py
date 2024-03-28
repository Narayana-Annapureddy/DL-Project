import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

dates, new_cases, total_cases, active_cases, daily_deaths, recovered=[],[],[],[],[],[]
t_ignore='        \t\n'
months={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun',
        '07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
###DEFINING TOKENS###
tokens = ('TOTALCASES','NEWCASES','CATEGORIES','ACTIVECASES','DAILYDEATHS','RECOVERED','LINEWIDTH','LINEAR','CHECKBOX','OPENTABLE', 'OPENHEAD','CLOSEHEAD','CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF','SPACE','CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN','CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')

###############Tokenizer Rules################
def t_TOTALCASES(t):
     r"text:.'Total.Cases'"
     return t

def t_NEWCASES(t):
     r"text:.'Daily.New.Cases'"
     return t

def t_CATEGORIES(t):
    r'categories'
    return t

def t_ACTIVECASES(t):
    r"name:.'Currently.Infected'"
    return t

def t_DAILYDEATHS(t):
    r"name:.'Daily.Deaths',"
    return t

def t_RECOVERED(t):
    r"name:.'New.Recoveries',"
    return t

def t_LINEWIDTH(t):
    r'lineWidth:.5'
    return t

def t_LINEAR(t):
    r"Linear.Scale"
    return t

def t_CHECKBOX(t):
    r'showCheckbox:'
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
    r'[A-Za-z0-9+,.\/\u00E9\-" ]+'
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
    '''table : TOTALCASES skiptag LINEAR skiptag CATEGORIES CONTENT skiptag LINEWIDTH CONTENT CONTENT CONTENT
             | NEWCASES newcases
             | ACTIVECASES skiptag LINEWIDTH CONTENT CONTENT CONTENT
             | DAILYDEATHS skiptag CHECKBOX CONTENT CONTENT CONTENT
             | RECOVERED skiptag LINEWIDTH CONTENT CONTENT CONTENT'''
    global dates, total_cases,active_cases, daily_deaths, recovered
    if len(p)==12:
        dates=p[6].replace(',','').split('""')
        dates[0]=dates[0].replace('"','')
        dates[-1]=dates[-1].replace('"','')
        total_cases=p[11].split(',')
    elif len(p)==7: 
        #print(p[1])
        if p[1].find('Currently Infected')!=-1: active_cases = p[6].split(',')
        elif p[1].find('Recoveries')!=-1: recovered = p[6].split(',')
        else: daily_deaths = p[6].split(',')

def p_newcases(p):
    '''newcases : skiptag CATEGORIES CONTENT skiptag CHECKBOX skiptag CHECKBOX CONTENT CONTENT CONTENT'''
    global new_cases
    if len(new_cases)==0: new_cases = p[10].split(',')

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | SPACE skiptag
               | empty'''

def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : CONTENT content
               | empty'''
    p[0]=p[1]+p[2]
    if len(p)==3:
        print(p[1])

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

def extractData(country):
    file_obj= open(f'data/{country}/webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    file_obj.close()
    parse(data)

def getData(country, url):
    global dates, total_cases,active_cases, daily_deaths, recovered, new_cases
    dates.clear()
    total_cases.clear()
    active_cases.clear()
    daily_deaths.clear()
    recovered.clear()
    new_cases.clear()
    downloadWebPage(url,f'data/{country}/webpage.html')
    extractData(country)
    arr=[active_cases, daily_deaths, new_cases, recovered]
    file = open(f'data/{country}/data.txt','w')
    file.write('Date\tActive Cases\tDaily Death\tNew cases\tRecoverd Cases\n')
    arr=[active_cases, daily_deaths, new_cases, recovered]
    for i in range(len(arr)):
        if len(arr[i])==0: arr[i] = ['0' for j in range(len(dates))]
        for j in range(len(arr[i])):
            x = arr[i][j]
            if (x=='' or x=='NA'or x=='null'or x=='N/A'):
                arr[i][j]='0'

    for i in range(len(dates)):
        string = dates[i]+'\t'+arr[0][i]+'\t'+arr[1][i]+'\t'+arr[2][i]+'\t'+arr[3][i]
        file.write(string+'\n')
    file.close()
    file=None

#########DRIVER FUNCTION#######
def main():
    global dates, total_cases,active_cases, daily_deaths, recovered
    file = open('data1.txt','r')
    countries= file.readlines()
    for ip in countries:
        country_data = ip.split('\t')
        country,url=country_data[0].strip(), country_data[1]
        print(country)
        if country=='Country Name' or country.lower()=='world': continue
        getData(country.lower(),f'https://www.worldometers.info/coronavirus/{url}')
  
if __name__ == '__main__':
    main()