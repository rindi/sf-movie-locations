from django.http import HttpResponse
from locations.models import Location, Movie

def index(request):
    movie_list = Movie.objects.order_by('title')
    output = '<li>'.join([m.title for m in movie_list])
    return HttpResponse(output)