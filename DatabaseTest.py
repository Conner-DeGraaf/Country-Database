from CountryDatabase import CountryDatabase

def print_list(lst):
    for i in lst:
        print(i)
    print(f"\nThere are {len(lst)} results...")




database = CountryDatabase()
database.import_data()

''' Number of countries in the 

print(f"There are {database.count_countries()} countries")
'''

# Searches for a country in the database
#lst = database.search_country("a")
#print_list(lst)


''' Finds the capital of a country otherwise prints there is none.

country = "Antartica"
capital = database.country_capital(country)
if capital == None:
    print(f"\nThere is no captial of {country}")
else:
    print(f"\nThe capital of {country} is {capital}")
'''

# Finds populations greater of less than number provided.
# populations = database.search_population(1000000000, "greater")
# print_list(populations)

''' Finds all the areas greater than or less than the area provided. 
 
areas = database.search_area(14000000, "greater")
print_list(areas)
'''

# Will Find the greatest or least population size
#direction = "least"
#location = database.population_extreme(direction)
#print(f"This is the country with the {direction} population size:")
#print(location)

''' Will Find the greatest or least area (km)

direction = "greatest"
location = database.area_extreme(direction)
print(f"This is the country with the {direction} area:")
print(location)
'''