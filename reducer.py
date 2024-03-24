import sys
prev_key=None
combined=[]
country=''
value_countrys={}

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if (len(value)==0 and value[0].find('_')==-1): 
        country= value[0]
    if key in value_countrys:
        val = value_countrys.get(key) + value.split('#')
        value_countrys[key] =  val
    else: value_countrys[key] = value.split('#')

print(country)
for key in value_countrys.keys():
    values = value_countrys.get(key)
    for val in values:
        if val.find(country)!=-1: print(f'f{val}: {key}')
#print(value_countrys)
    #print(line)