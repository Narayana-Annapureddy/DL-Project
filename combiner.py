import sys
world_data=[]
value_countrys={}


for line in sys.stdin:
    if line.find(',')==-1: continue
    key,value = line.strip().split(',')
    if value in value_countrys: value_countrys.get(value).append(key)
    else: value_countrys[value]= [key]

for key in value_countrys.keys():
    value = '#'.join(value_countrys[key])
    try:
        print(f'{float(key)}\t{value}')
    except:
        print(f'{key}\t{value}')