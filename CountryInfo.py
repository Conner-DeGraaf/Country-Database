
class CountryInfo():
    def __init__(self, name, capital, population, area):
        self.country = name
        self.capital = capital
        self.population = int(population)
        self.area = float(area)

    def get_country(self):
        return self.country
    
    def get_capital(self):
        return self.capital

    def get_population(self):
        return self.population
    
    def get_area(self):
        return self.area
    
    def __str__(self):
        string = (f"\n{self.country}\t-->\tPopulation:{self.population}\tArea:{self.area}")
        return string