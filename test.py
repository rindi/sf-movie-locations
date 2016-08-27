from locations.models import Location, Movie
import csv
movies = set()
with open('Film_Locations_in_San_Francisco.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title=row['Title']
        if title in movies:
            continue
        else:
            movies.add(title)
            movie = Movie.objects.create(title=row['Title'], release_year=row['Release Year'], production_company=row['Production Company'], distributor=row['Distributor'], director=row['Director'], writer=row['Writer'], actor1=row['Actor 1'], actor2=row['Actor 2'], actor3=row['Actor 3'])
            movie.save()
    print "Done"