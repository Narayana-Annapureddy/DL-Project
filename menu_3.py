<<<<<<< HEAD:menu_3.py
from module3_1 import task3_2
from module3_1 import task3
from module1 import task1
import os
import subprocess

mapper_cmd="python3 mapper.py worldometers_countrylist.txt | python3 combiner.py | sort -n | python3 reducer.py"
def main():
    #task1.main()
    #task3.main()
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
            subprocess.call('make', cwd='module3_1')
        elif(query==5): task3_2.extract_4_casesas()
        elif(query==-1): break
        else: print("Invalid query, pls try again")

if __name__ == '__main__':
=======
from module3_1 import task3_2
from module3_1 import task3
from module1 import task1
import os
import subprocess

mapper_cmd="python3 mapper.py worldometers_countrylist.txt | python3 combiner.py | sort -n | python3 reducer.py"
def main():
    #task1.main()
    #task3.main()
    while(True):
        print("Queries")
        print('1. TO print Active, daily death, new cases, new recovered given country')
        print('2. To print the percentage of cases withrect to world')
        print('3. To find change in percentage')
        print('-1. Exit')
        query=int(input("\nEnter query no: "))
        if(query==2): 
            task3_2.print_all_countries_data()
        elif(query==3):
            country=input("Enter Country name: ")
            start_date =input("Enter start date in dd-mm-yyyy format: ")
            end_date =input("Enter end date in dd-mm-yyyy format: ")
            file = open("input.txt",'w')
            file.write(country+'\t'+start_date+'\t'+end_date)
            file.close()
            subprocess.call('make', cwd='module3_1')
        elif(query==1): task3_2.extract_4_cases()
        elif(query==-1): break
        else: print("Invalid query, pls try again")

if __name__ == '__main__':
>>>>>>> 55f95e5f7dbe6d1e1236db244642aa9c4f69b4c5:menu.py
    main()