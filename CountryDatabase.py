from CountryInfo import CountryInfo
from bs4 import BeautifulSoup
import requests

class CountryDatabase():
    def __init__(self):
        self.countries = {}

    def import_data(self):
        page = requests.get("https://www.scrapethissite.com/pages/simple/")
        soup = BeautifulSoup(page.text, 'html.parser')
        country_names = soup.find_all("h3", attrs={"class":"country-name"})
        capitals = soup.find_all("span", attrs={"class":"country-capital"})
        populations = soup.find_all("span", attrs={"class":"country-population"})
        areas = soup.find_all("span", attrs={"class":"country-area"})

        for i in range(len(country_names)):
            self.countries[country_names[i].text.strip()] = CountryInfo(country_names[i].text.strip(), capitals[i].text.strip(), populations[i].text.strip(), areas[i].text.strip())
    
    def count_countries(self):
        return len(self.countries)
    
    def search_country(self, name):
        name = name.upper()
        result = []

        for object in self.countries.values():
            country = object.get_country().upper()
            if country.find(name) != -1:
                result.append(object)
            

        return result
        
    def country_capital(self, name):
        name = name.upper()
        result = None

        for object in self.countries.values():
            country = object.get_country().upper()
            if country == name:
                result = object.get_capital()
            
        return result

    def search_population(self, number, value):
        lst = []
        for object in self.countries.values():
            if value == "greater":
                if object.get_population() >= number:
                    lst.append(object)
            elif value == "less":
                if object.get_population() <= number:
                    lst.append(object)
            else:
                lst = []
        return lst

    def search_area(self , number, value):
        lst = []
        for object in self.countries.values():
            if value == "greater":
                if object.get_area() >= number:
                    lst.append(object)
            elif value == "less":
                if object.get_area() <= number:
                    lst.append(object)
            else:
                lst = []
        return lst

    def population_extreme(self, value):
        min_obj = None
        max_obj = None
        max = 0
        min = 100000

        for object in self.countries.values():
            
            if object.get_population() > max:
                max_obj = object
                max = object.get_population()

            if object.get_population() < min:
                min_obj = object
                min = object.get_population()

        if value == 'greatest':
            result = max_obj
        elif value == 'least':
            result = min_obj
        
        return result

    def area_extreme(self, value):
        min_obj = None
        max_obj = None
        max = 0
        min = 100000

        for object in self.countries.values():
            
            if object.get_area() > max:
                max_obj = object
                max = object.get_area()

            if object.get_area() < min:
                min_obj = object
                min = object.get_area()

        if value == 'greatest':
            result = max_obj
        elif value == 'least':
            result = min_obj
        
        return result