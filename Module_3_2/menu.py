import subprocess
import os

def main():

    while True:
        
        print("Enter query range from 2-5:")
        print("2. To get worldwide news and responses.")
        print("3. To get date range for which news information is available for that country.")
        print("4. The news between the time duration for a given country.")
        print("5. Jaccard similarity between two countries.")
        print("-1. Exit.....")

        query = int(input("\nEnter your query: "))
        file = ""
        if (query == 2):
            start_date = input("Enter the start date: ")
            end_date = input("Enter the end date : ")
            file = f"{os.getcwd()}/Module_3_2/task1/run.py"
            os.system(f"python3 {file} {start_date} {end_date}")

        elif (query == 3):
            country = input("Enter country name : ")
            file = f"{os.getcwd()}/Module_3_2/task2/run.py"
            os.system(f"python3 {file} {country}")

        elif (query == 4):
            country = input("Enter the country name : ")
            start_date = input("Enter the start date: ")
            end_date = input("Enter the end date : ")
            file = f"{os.getcwd()}/Module_3_2/task3/run.py"
            os.system(f"python3 {file} {country} {start_date} {end_date}")

        elif (query == 5):
            country = input("Enter the country name : ")
            start_date = input("Enter the start date: ")
            end_date = input("Enter the end date : ")
            file = f"{os.getcwd()}/Module_3_2/task4/run.py"
            os.system(f"python3 {file} {country} {start_date} {end_date}")
            
        elif (query == -1):
            break

        else:
            print("Invalid query number...\n")

        print(file)
        

if __name__ == '__main__':
    main()
