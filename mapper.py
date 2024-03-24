import sys
import task3
file = open(sys.argv[1],'r')

start_date='10-10-2020'
end_date='12-11-2021'
country='china'
global_url='https://www.worldometers.info/coronavirus/'

print(f'{country.lower()},{-9999999999999}')

for line in file:
    if line.find(',')==-1: continue
    row = line.strip().split(',')
    if len(row)==0: continue
    key,url = row[1],row[2]
    if url.find('country/')==-1: continue
    values=task3.getData(key, global_url+url, start_date, end_date, 'all')  #[active, daily, new, recovery]
    queries=['active','death','new','recovery']
    for i in range(4):  print(f'{key.lower()}_{queries[i]},{values[i]}')
