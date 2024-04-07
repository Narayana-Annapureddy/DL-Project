import os, sys
from datetime import datetime

def main():

    print(sys.argv)
    county = sys.argv[1]
    # country = 'england',  start_date = '2-1-2022',  end_date = '5-1-2023'
    
    if (county == 'australia'):
        file_list = ['australia_2020.txt', 'australia_2022.txt', 'australia_January_June_2021.txt', 'australia_July_December_2021.txt']
    elif (county == 'england'):
        file_list = ['england_2021.txt', 'england_2022.txt', 'england_January_June_2020.txt', 'england_July_December_2020.txt']
    elif (county == 'india'):
        file_list = ['india_2021.txt', 'india_January_May_2020.txt', 'india_June_December_2020.txt']
    elif (county == 'malaysia'):
        file_list = ['malaysia_2020.txt', 'malaysia_2021.txt', 'malaysia_2022.txt', 'malaysia_2023.txt', 'malaysia_2024.txt']
    elif (county == 'singapore'):
        file_list = ['singapore_2020.txt', 'singapore_2021.txt', 'singapore_2022.txt']


    start_date = sys.argv[2]
    end_date = sys.argv[3]

    makefileCmd = "("
    for file in file_list:
        makefileCmd += f'(python3 mapper.py {file} | sort -n | python3 combiner.py; wait) &'
        
    makefileCmd = makefileCmd[:-2]
    makefileCmd += f") | sort -n | python3 reducer.py {start_date} {end_date} > result.txt"
    #print(makefileCmd)
    os.system(makefileCmd)
   

main()
