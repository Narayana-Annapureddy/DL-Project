base_url = "https://en.wikipedia.org/wiki/"
page_name = "Timeline_of_the_COVID-19_pandemic_in_"
 
countries = {
    "india": ["(January%E2%80%93May_2020) January_May_2020", "(June%E2%80%93December_2020) June_December_2020", "(2021) 2021"],
    "malaysia": ["(2020) 2020", "(2021) 2021", "(2022) 2022", "(2023) 2023", "(2024) 2024"],
    "singapore": ["(2020) 2020", "(2021) 2021", "(2022) 2022"],
    "australia": ["(2020) 2020", "(January%E2%80%93June_2021) January_June_2021", "(July%E2%80%93December_2021) July_December_2021", "(2022) 2022"],
    "england": ["(January%E2%80%93June_2020) January_June_2020", "(July%E2%80%93December_2020) July_December_2020", "(2021) 2021", "(2022) 2022"]
}
 
# Open the file for writing
with open("countrylinks.txt", "w") as file:
    for country, years in countries.items():
        file.write(f"{country}\n")
        country = country.capitalize()
       
        for year in years:
            link = base_url + page_name + country + f"_{year}"
            file.write(f"{link}\n")