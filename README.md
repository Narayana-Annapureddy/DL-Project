I have done 
Remaining modules are done by my teammates Narayana, Akash.



Vamsi (23CS60R66) : Module1, Module 3.1 \n
Narayana (23CS60R40) : Module 3.2, Main menu driven program\n
Akash (23CS60R14) : Module 2\n







# task1.py
In this file we are extracting the world covid data information and storing this info in data1.txt
compile using 

python3 task1.py

# task3.py
In this file we are redaing each country name from the world list and getting the data from their country website and storing them in data/{country name}/data.txt
compile using 

python3 task3.py

# task3_2.py
In this file we are calculating the module 3.1 query2, module 1 query.
run program using 

python3 task3_2.py

# Compilation steps for module 3.1
If we want to change country name, dates. As of now we will give these at compile time in mapper.py file. Integration is pending. while doinf integration of entire code, we will change this to give parametes at runtime.


python3 mapper.py worldometers_countrylist.txt | python3 combiner.py | sort -n | python3 reducer.py
