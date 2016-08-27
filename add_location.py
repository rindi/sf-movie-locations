from locations.models import Location, Movie
import csv

with open('Film_Locations_in_San_Francisco.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_title=row['Title']
        location = Location.objects.create(locations=row['Locations'], movie=Movie.objects.filter(title=movie_title)[0])
        location.save()

        