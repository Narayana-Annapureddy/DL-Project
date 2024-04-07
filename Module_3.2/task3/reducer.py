import sys, re
from datetime import datetime

current_date = None
prev_date = None
finalValue = ""

start_date = sys.argv[1]
end_date = sys.argv[2]


def req_range(start_date, end_date, date):
    try:
        start_date = datetime.strptime(start_date[start_date.find('-')+1:], "%m-%Y")
        end_date = datetime.strptime(end_date[end_date.find('-')+1:], "%m-%Y")
        date = datetime.strptime(date[date.find('-')+1:], "%m-%Y")
        return start_date <= date <= end_date
    except:
        pass


for line in sys.stdin:

    value = ""
    try:
        current_date, value = line.split('$$')
    except:
        pass

    if (current_date == prev_date):
        finalValue += '#' + str(value)
        value = ""
    else:
        if (prev_date != None):
                
            if (req_range(start_date, end_date, prev_date)):
                print(f'{prev_date[3:]}.....')
                for data in finalValue.split('#'):
                    print(data)
                print('\n\n')
        
        prev_date = current_date
        finalValue = str(value)
    

if (prev_date != None):
   

    if (req_range(start_date, end_date, prev_date)):
        print(f'{prev_date[3:]}.....')
        for data in finalValue.split('#'):
            print(data)
        print('\n\n')
