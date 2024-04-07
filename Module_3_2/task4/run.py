import os
import sys

def main():

    countryList = ['australia', 'malaysia', 'england', 'india', 'singapore']
    country = sys.argv[1]
    start_date =  sys.argv[2]
    end_date = sys.argv[3]
    
    cmd = f'python3 {os.getcwd()}/Module_3_2/task4/helper.py {country} {start_date} {end_date}'
    print(cmd)
    os.system(cmd)

    country_words = set()
    fp = open(f'result.txt', 'r')
    for line in fp.readlines():
        for word in line.split():
            country_words.add(word)
    fp.close()
    jaccardIndex, maxSim = 0.0, -float('inf')
    ans = None

    
    
    for c in countryList:

        if c == country:
            continue
        
        try:
            cmd = f'python3 {os.getcwd()}/Module_3_2/task4/helper.py {c} {start_date} {end_date}'
            os.system(cmd)
        except:
            print(cmd)
        
        
        other_country_words = set()
        fp = open(f'result.txt', 'r')
        for line in fp.readlines():
            for word in line.split():
                other_country_words.add(word)
    
        try:
            s1 = country_words
            s2 = other_country_words
            size_s1 = len(s1); 
            size_s2 = len(s2); 
            print(size_s1, size_s2)
            intersect = s1 & s2 
            size_in = len(intersect); 

            jaccardIndex = size_in  / (size_s1 + size_s2 - size_in)
            
        except:
            jaccardIndex = 0.0

        print(maxSim, jaccardIndex)
        if (maxSim < jaccardIndex):
            maxSim = jaccardIndex
            ans = c

    print(f'The country {ans} is similar to country {country} with similarity {maxSim}')

main()
