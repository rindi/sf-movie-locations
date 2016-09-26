from django.test import TestCase
from locations.models import Location, Movie

class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="Zxcvbnm", release_year="2016")
        movie = Movie.objects.get(title="Zxcvbnm")
        movie_id = movie.id
        Location.objects.create(locations="1600 Holloway Av.", movie_id=movie_id)

    def test_movie(self):
        movie = Movie.objects.get(title="Zxcvbnm")
        movie_id = movie.id
        location = Location.objects.get(movie_id=movie_id)
        self.assertEqual(movie.release_year, 2016)
        self.assertEqual(location.locations, "1600 Holloway Av.")
