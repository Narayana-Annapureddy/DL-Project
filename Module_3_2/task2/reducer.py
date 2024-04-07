import sys

months = ['January','February','March','April','May','June',
            'July','August','September','October','November','December']

arr = []

def get_least_max(finalValue):
    temp = finalValue.split('$$')
    return temp[0], temp[1].strip()
        

current_date = None
prev_date = None
finalValue = 0

for line in sys.stdin:

    if not line:
        continue

    current_date, value = line.split('#')
    if (current_date == prev_date):
        finalValue += '$$' + value
    else:
        if (prev_date != None):
            least, max = get_least_max(finalValue)
            arr.append([prev_date, least, max])
        
        prev_date = current_date
        finalValue = value

if (prev_date != None):
    least, max = get_least_max(finalValue)
    arr.append([prev_date, least, max])


arr.sort()
print(arr)
print(f'{arr[0][1]}-{arr[0][0]}, {arr[-1][2]}-{arr[-1][0]}')
