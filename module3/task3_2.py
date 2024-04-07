def extract_4_cases():
    dict_data={}
    file = open("data1.txt",'r')
    for line in file:
        data=line.replace('\n','').split('\t')
        dict_data[data[0].lower()] = data[2:]

    while(True):
        ip=input("Enter country name(-1 for exit): ")
        if(ip=="-1"): break
        if ip.lower() not in dict_data.keys():
            print("INvalid country name, pls try other name")
            continue
        data = dict_data[ip.lower()]
        active, daily,recovered,new = data[1],data[-2],data[-1],data[-3]
        print(f'Active Cases: {active}\nDaily Deaths: {daily}\nNew Recovered: {recovered}\nNew Cases:{new}')

def print_all_countries_data():
    data = open('data1.txt','r').readlines()
    arr=['Total cases',	'Active Cases','Total Deaths','Totat Recovered','Total Tests','Deaths/million', 'Tests/million','New Cases','New Death','New Recovery']
    total=data[1].split('\t')[2:]
    
    for i in range(len(total)):
        total[i]=float(total[i].replace('\n',''))
        if (total[i]==0): total[i]=1

    for j in range(2,len(data)):
        country = data[j]
        values = country.split('\t')
        print(values[0])
        for i in range(10):
            val = values[i+2].replace('+','')
            val = val.replace('\n','')
            if (val=='N/A' or val==''): val=0
            print(f'{arr[i]} {(int(val)/total[i])*100}%')
        print('\n')


def main():
    print_all_countries_data()
    extract_4_cases()

if __name__ == '__main__':
    main()