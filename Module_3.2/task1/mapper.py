import sys

file = sys.argv[1].strip()
fp = open(file, 'r')
key, val = None, None

for line in fp.readlines():

    line = line.strip()
    if not line:
        continue
    if line.startswith('_') or line[0].isdigit():
        key=line.strip('_')
    else:
        val=line
    
    if key and val:
        print(f'{key}${val}')
        key, value = None, None
