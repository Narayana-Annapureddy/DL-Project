import sys, re
from datetime import datetime

current_date = None
prev_date = None
finalValue = ""

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
            print(f'{prev_date}.....')
            for data in finalValue.split('#'):
                print(data)
            print('\n\n')
        
        prev_date = current_date
        finalValue = str(value)
    

if (prev_date != None):
    print(f'{prev_date}.....')
    for data in finalValue.split('#'):
        print(data)
    print('\n\n')
