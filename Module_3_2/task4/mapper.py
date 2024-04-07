import sys
import os

file = f"{os.getcwd()}/module2/{sys.argv[1].strip()}"
fp = open(file, 'r')
year = file[-5:-9:-1][::-1]
key, val = None, None

month_num = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
            'July':7,'August':8,'September':8,'October':10,'November':11,'December':12}

for line in fp.readlines():
    
    line = line.strip()
    if not line:
        continue
    try :

        new_line = line.strip(' _').split()
        if new_line[0] in month_num and len(new_line) <= 2:
            key = f"01-{month_num[new_line[0]]}-{year}"

        elif new_line[1] in month_num and len(new_line) <= 2:
            key = f"01-{month_num[new_line[1]]}-{year}"

        else:
            val = line.strip()

        if key and val:
            print(f"{key}${val}")
            key, val =  None, None

    except:
        pass
