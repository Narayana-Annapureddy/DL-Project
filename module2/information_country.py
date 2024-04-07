import info_country

def read_country_links():
    fp = open("countrylinks.txt","r")
    data  = fp.read()
    data = data.strip()
    data = data.split("\n")

    dic = {}
    for i in data:
        if(len(i)<10):
            if(dic.get(i) is None):
                dic[i] = []
            name = i
        else: 
            dic[name].append(i)
    return dic

def get_data_by_countryname(cname):
    country_links = read_country_links()
    print(country_links)
    cname=cname.lower()
    if cname in country_links:
        for item in country_links[cname]:
            info_country.main(item.split(" ")[0],cname+"_"+item.split(" ")[1])
    else:
        print(f"Country name '{cname}' not found in the list.")

while(True):
    print("enter country name (Australia, England, India, Malaysia,singapore) enter exit to exit")
    cname = input()
    if(cname=="exit"):
        break
    get_data_by_countryname(cname)