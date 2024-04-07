import sys

months = ['January','February','March','April','May','June',
            'July','August','September','October','November','December']

def get_least_max(finalValue):
    
    least, max = None, None
    temp = finalValue.split()
    for month in months:
        if month in temp:
            least = month
            break
    
    for month in months[::-1]:
        if month in temp:
            return least, month

current_date = None
prev_date = None
finalValue = ""

for line in sys.stdin:

    current_date, value = line.split('$')
    if (current_date == prev_date):
        finalValue += ' ' + value
    else:
        if (prev_date != None):
            #print(prev_date, finalValue)
            least, max = get_least_max(finalValue)
            print(f'{prev_date}#{least}$${max}')
        
        prev_date = current_date
        finalValue = value

if (prev_date != None):
    #print(prev_date, finalValue)
    least, max = get_least_max(finalValue)
    print(f'{prev_date}#{least}$${max}')
