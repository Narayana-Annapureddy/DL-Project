import sys
import os

file = f"{os.getcwd()}/module2/{sys.argv[1].strip()}"

fp = open(file, 'r')
key, val = file[-5:-9:-1][::-1], ""

months = ['January','February','March','April','May','June',
            'July','August','September','October','November','December']

for line in fp.readlines():

    line = line.strip()
    if not line:
        continue
    try :

        if line.strip('_').split()[0] in months:
            val = line.strip('_')
            print(f'{key}${val}')

        elif line.strip('_').split()[1] in months:
            val = line.strip('_')
            print(f'{key}${val}')
    except:
        pass
