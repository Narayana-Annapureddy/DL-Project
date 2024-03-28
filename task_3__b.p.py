
def main():
    total=[0 for i in range(10)]
    data = open('data1.txt','r').readlines()
    for j in range(2,len(data)):
     country = data[j]
     values = country.split('\t')
     for i in range(2,len(values)):
        val = values[i].replace('+','')
        val = val.replace('\n','')
        if (val=='N/A' or val==''): val=0
        total[i-2]+=int(val)
    print(total)

    arr=['Total cases',	'Active Cases','Total Deaths','Totat Recovered','Total Tests','Deaths/million', 'Tests/million','New Cases','New Death','New Recovery']
    total=data[0].split('\t')[1:]
    for j in range(2,len(data)):
        country = data[j]
        values = country.split('\t')
        print(values[0])
        for i in range(10):
            val = values[i+2].replace('+','')
            val = val.replace('\n','')
            if (val=='N/A' or val==''): val=0
            print(f'{arr[i]} {int(val)/total[i]}')
        print('\n')
    
    
    #print(total)

if __name__ == '__main__':
    main()