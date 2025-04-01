from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(page.text, 'html.parser')
country_names = soup.find_all("h3", attrs={"class":"country-name"})
capitals = soup.find_all("span", attrs={"class":"country-capital"})
populations = soup.find_all("span", attrs={"class":"country-population"})
areas = soup.find_all("span", attrs={"class":"country-area"})

countries = {}

for i in range(len(country_names)):
    lst = [capitals[i].text, populations[i].text, areas[i].text]
    countries[country_names[i].text.strip()] = lst
print(countries)







