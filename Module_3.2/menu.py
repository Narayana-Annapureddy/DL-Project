import subprocess
import os

def main():

    while True:
        
        print("Enter query range from 2-5:")
        print("2. To get worldwide news and responses.")
        print("3. To get date range for which news information is available for that country.")
        print("4. The news between the time duration.")
        print("5. Jaccard similarity between two countries.")
        print("6. Exit.....")

        query = int(input("\n\nEnter your query: "))
        file = ""
        if (query == 2):
            start_date = input("Enter the start date: ")
            end_date = input("Enter the end date : ")
            file = os.path.join("task1", "run.py")
            params = [start_date, end_date]

        elif (query == 3):
            pass
        else:
            break

        subprocess.call(['python3', file] + params)

main()
