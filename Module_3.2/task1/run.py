import os
import sys
from datetime import datetime

month_num = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
            'July':7,'August':8,'September':8,'October':10,'November':11,'December':12}

def main():

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")

    
    # For getting the timeline news in the required date
    for year in ['2019', '2020', '2021', '2022', '2023', '2024']:

        makefileCmd = "("
        flag = False
        for month in month_num:     # running mapper, combiner, reducer year wise and store in sep txt file

            file =  f'{year}/{month}.txt'
            date = f'1-{month_num[month]}-{year}'
            date = datetime.strptime(date, "%d-%m-%Y")

            if not (start_date <= date <= end_date):
                continue

            if os.path.exists(file):
                flag = True
                makefileCmd += f'(python3 task1/mapper.py {file} | sort -n | python3 task1/combiner.py; wait) &'

        if flag:
            makefileCmd = makefileCmd[:-2]
            print(makefileCmd)
            makefileCmd += f") | sort -n | python3 task1/reducer.py > result_timeline_{year}.txt"
            os.system(makefileCmd)


    # For getting the timeline response in the required date
    for year in ['2019', '2020', '2021', '2022', '2023', '2024']:

        makefileCmd = "("
        flag = False
        for month in month_num:     # running mapper, combiner, reducer year wise and store in sep txt file

            file =  f'response_{year}/{month}.txt'
            date = f'1-{month_num[month]}-{year}'
            date = datetime.strptime(date, "%d-%m-%Y")

            if not (start_date <= date <= end_date):
                continue

            if os.path.exists(file):
                flag = True
                makefileCmd += f'(python3 task1/mapper.py {file} | sort -n | python3 task1/combiner.py; wait) &'

        if flag:
            makefileCmd = makefileCmd[:-2]
            print(makefileCmd)
            makefileCmd += f") | sort -n | python3 task1/reducer.py > result_response_{year}.txt"
            os.system(makefileCmd)

print("HI")
main()
