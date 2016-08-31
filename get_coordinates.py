import googlemaps
import csv

gmaps = googlemaps.Client(key='AIzaSyDgiFQgzH8KC23ls0oXhvGndEPh_Gz3GHI')

with open('Film_Locations_in_San_Francisco.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_location = row['Locations']
        location = geolocator.geocode(movie_location+" San Francisco")
        break
        # print(location.address)
        # print((location.latitude, location.longitude))
