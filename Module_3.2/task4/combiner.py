import sys

current_date = None
prev_date = None
finalValue = 0

for line in sys.stdin:
    
    current_date, value = line.split('$')
    if (current_date == prev_date):
        finalValue += '#' + value
    else:
        if (prev_date != None):
            print(f'{prev_date}$${finalValue}')
        
        prev_date = current_date
        finalValue = value

print(f'{prev_date}$${finalValue}')
