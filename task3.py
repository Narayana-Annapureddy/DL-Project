import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

dates, new_cases, total_cases, active_cases, daily_deaths, recovered=[],[],[],[],[],[]
t_ignore='        \t\n'
months={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun',
        '07':'Jul','08':'Sep','09':'Oct','10':'Oct','11':'Nov','12':'Dec'}
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

def extractData():
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    file_obj.close()
    parse(data)

def getFormatedDate(date):
    arr=date.split('-')
    formatted_date =  months[arr[1]]+' '+arr[0]+' '+arr[2]
    ind =dates.index(formatted_date)
    #print(formatted_date+',  '+str(ind))
    return ind

def checkRate(s,e) :
    try:
        if (int(s)==0 or s=='0'): return e
        else: return round(((int(s)-int(e))/int(s))*100,3)
    except:
        print(f'except {s} {e}')

def getData(country, url, start_date, end_date, query):
    global dates, total_cases,active_cases, daily_deaths, recovered
    downloadWebPage(url,'webpage.html')
    extractData()
    val=[]
   
    start_ind, end_ind = getFormatedDate(start_date), getFormatedDate(end_date)
    arr=[active_cases, daily_deaths, new_cases, recovered]
    for i in range(len(arr)):
        #print(arr[i])
        for j in range(len(arr[i])):
            x = arr[i][j]
            if (x=='' or x=='NA'or x=='null'or x=='N/A'):
                arr[i][j]='0'
        #print(arr[i])
    #active_cases, daily_deaths, new_cases, recovered = arr[0],arr[1],arr[2],arr[3]
            
    val.append(checkRate(arr[0][start_ind], arr[0][end_ind]))
    val.append(checkRate(arr[1][start_ind], arr[1][end_ind]))
    val.append(checkRate(arr[2][start_ind], arr[2][end_ind]))
    val.append(checkRate(arr[3][start_ind], arr[3][end_ind]))
    #elif query=='all': return f'{checkRate(active_cases[start_ind], active_cases[end_ind])}#{checkRate(daily_deaths[start_ind], daily_deaths[end_ind])}#{checkRate(new_cases[start_ind], new_cases[end_ind])}#{checkRate(recovered[start_ind], recovered[end_ind])}'
    return val
    out = f'{country} {len(dates)} {len(total_cases)} {len(new_cases)} {len(active_cases)} {len(daily_deaths)} {len(recovered)}\n'
    out1 = f'{active_cases[start_ind]} {daily_deaths[start_ind]} {new_cases[start_ind]} {recovered[start_ind]}'
    out2 = f'{active_cases[end_ind]} {daily_deaths[end_ind]} {new_cases[end_ind]} {recovered[end_ind]}'
    print(out)
    print(out1)
    print(out2)


#########DRIVER FUNCTION#######
def main():
    global dates, total_cases,active_cases, daily_deaths, recovered
    #view-source:https://www.worldometers.info/coronavirus/country/greenland/
    country,url='france','country/china/'
    start_date = input('Enter date in dd-mm-yyyy format: ')
    end_date = input('Enter date in dd-mm-yyyy format: ')
    getData(country,f'https://www.worldometers.info/coronavirus/{url}', start_date, end_date,'all')


  
if __name__ == '__main__':
    main()