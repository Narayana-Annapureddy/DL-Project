import os
country_file = open('../worldometers_countrylist.txt','r')
countries= country_file.readlines()

for ip in countries:
    country=ip.replace('\n','').lower()
    os.makedirs(country)
