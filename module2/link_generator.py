links = []

for year in [2019,2023,2024]:
    links.append(f'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_{year}" title="Timeline of the COVID-19 pandemic in {year}">')
for month in range(2022, 2019,-1):
    for month_name in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
        links.append(f'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_{month_name}_{month}" title="Timeline of the COVID-19 pandemic in {month_name} {month}">')


with open("timelinelinks.txt", "w") as f:
    for link in links:
        f.write(f"{link}\n")

response_list=[]     
for year in range(2022,2019,-1):
    for month_name in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
        if year==2022 and month_name in ['November','December']:
            continue
        else:
            linki=f'<a href="/wiki/Responses_to_the_COVID-19_pandemic_in_{month_name}_{year}" title="Responses to the COVID-19 pandemic in {month_name} {year}">'
            
            response_list.append(linki)
with open("responselinks.txt", "w") as f:
    for link in response_list:
        f.write(f"{link}\n")