import sys

country, closest_country, closest_value, percent='','',1000000000,0
cases_types, percentages=[[],[],[],[]], [[],[],[],[]] #[active, new, death, recover]

type=['Active Cases','New Cases','Daily Death','Recovery']

dictionary={
    'new':'New Cases',
    'death':'Daily Death',
    'recovery':'New Recovered Cases',
    'active':'Active Cases'
}

def add_to_list(percent, countries):
    index=-1  #[active, new, death, recover]
    for country in countries.split('#'):
        #if (country.find('india')!=-1):
            #print(f'{country} {percent}')
        if (country.find('active')!=-1): index=0
        elif (country.find('new')!=-1): index=1
        elif (country.find('death')!=-1): index=2
        elif (country.find('recovery')!=-1): index=3
        percentages[index].append(float(percent))
        cases_types[index].append(country.split('_')[0])

def closest(ind1, ind2, values, countries, case_type):
    global closest_country, closest_value
    if (abs(values[ind1]-values[ind2]) < closest_value):
            closest_value = abs(values[ind1]-values[ind2])
            closest_country = countries[ind1]+' '+ case_type
            return 1
    else: return 0
    

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if (value.find('_')==-1): 
        country= value
        continue
    add_to_list(key, value)


for i in range(4):
    index = cases_types[i].index(country)
    values = percentages[i]
    print(f'Change in {type[i]}%: {values[index]} ')
    if (index>0 and index<len(cases_types[i])-1): 
        closest(index-1, index, values, cases_types[i], type[i])
        closest(index+1, index, values, cases_types[i], type[i])
    elif (index>0): closest(index-1, index, values, cases_types[i])
    else: closest(index+1,index, values, cases_types[i], type[i])

print(f'Closest Country: {closest_country}')   
#print(closest_value)