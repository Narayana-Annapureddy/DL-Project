import sys
file = open(sys.argv[1],'r')

ip = open("input.txt",'r')
country, start_date, end_date = ip.read().split('\t')
#print(country, start_date, end_date)
months={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun',
        '07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}

def getFormatedDate(date):
    arr=date.split('-')
    formatted_date =  months[arr[1]]+' '+arr[0]+' '+arr[2]
    return formatted_date

def checkRate(s,e) :
    if (s==0): return e
    else: return round(((e-s)/s)*100,3)
   
print(f'{country.lower()},{-9999999999999}')

def get_percentages(country):
    data = open(f'data/{country}/data.txt','r').readlines()
    start_data, end_data, percentages=[],[],[]
    for day in data:
        date = day.replace('\n','').split('\t')[0]
        if (date==formated_start_date): start_data = day.replace('\n','').split('\t')
        if (date==formated_end_date): end_data = day.replace('\n','').split('\t')
    for i in range(1,5): percentages.append(checkRate(int(start_data[i]),int(end_data[i])))
    return percentages

formated_start_date, formated_end_date = getFormatedDate(start_date), getFormatedDate(end_date)

for country in file:
    key = country.replace('\n','')
    if key.lower()=='world': continue
    percentages = get_percentages(key)
    queries=['active','death','new','recovery'] #arr=[active_cases, daily_deaths, new_cases, recovered]
    for i in range(4):  print(f'{key.lower()}_{queries[i]},{percentages[i]}')