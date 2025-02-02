# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __repr__(self):
    return f"<City name: {self.name}, lat: {self.lat}, lon: {self.lon}>"

  def __str__(self):
    return f"{self.name}: ({self.lat},{self.lon})"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

import csv

cities = []

def cityreader(cities=None):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  if cities is None:
    cities = []
  with open('cities.csv') as citiescsv:
    rows = csv.DictReader(citiescsv)
    for city in rows:
      cities.append(City(city["city"], float(city["lat"]), float(city["lng"])))
  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

input_1 = input("lat1,lon1: ").strip().split(",")
input_2 = input("lat2,lon2: ").strip().split(",")

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=None):
  # We don't need to run this on empty or null city lists
  if cities is None:
    return []
  
  # Cast all input's to floats
  lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
  corner1, corner2 = None, None

  # Swap longitudes if they are the wrong way around
  if lon1 > lon2:
    lon1, lon2 = lon2, lon1

  #Normalise to upper-left, lower-right
  if lat1 > lat2:
    corner1, corner2 = (lat1, lon1), (lat2, lon2)
  else:
    corner1, corner2 = (lat2, lon1), (lat1, lon2)
  
  def is_within(v1, v2, pos):
    if (v1[0] > pos[0] > v2[0]) and (v2[1] > pos[1] > v1[1]):
      return True
    else:
      return False

  #List comprehension running the is_within function on each city
  within = [city for city in cities if is_within(corner1, corner2, (city.lat, city.lon))]
  
  return within

for c in cityreader_stretch(input_1[0], input_1[1], input_2[0], input_2[1], cities):
    print(c)