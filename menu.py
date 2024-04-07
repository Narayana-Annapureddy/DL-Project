from module3 import task3_2
from module3 import task3
from module1 import task1
import os
import subprocess

mapper_cmd="python3 mapper.py worldometers_countrylist.txt | python3 combiner.py | sort -n | python3 reducer.py"
def main():

    while(True):
        query=int(input("Enter query no for NoSql (-1 for exit): "))
        if(query==2): 
            #task3_2.extract_4_cases()
            task3_2.print_all_countries_data()
        elif(query==3):
            country=input("Enter Country name: ")
            start_date =input("Enter start date in dd-mm-yyyy format: ")
            end_date =input("Enter end date in dd-mm-yyyy format: ")
            file = open("input.txt",'w')
            file.write(country+'\t'+start_date+'\t'+end_date)
            file.close()
            subprocess.call('make', cwd='module3')
        elif(query==-1): break
        else: print("Invalid query, pls try again")

if __name__ == '__main__':
    main()