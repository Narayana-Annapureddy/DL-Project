from module3_1 import task3
from module1 import task1
import menu_3
import os
from Module_3_2 import menu
from module2 import run_scripts

def main():

    # To run the lex files uncomment the below
    #task1.main()      
    #task3.main()
    #run_scripts.main()

    # To run the NoSQL queries in specific
    while True:
        print("1. To go to module_3.1")
        print("2. To go to module_3.2")
        print("-1. To exit")

        module = int(input("Enter your number : "))
        if (module == 1):
            menu_3.main()
        elif (module == 2):
            menu.main()
        elif (module == -1):
            break
        else:
            print("Invalid number...")
        print('\n')

main()
