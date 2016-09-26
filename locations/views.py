from django.http import HttpResponse
from locations.models import Location, Movie
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import MovieForm
import requests
import yaml

config_file = open('/static/config.yaml')
config = yaml.load(config_file)
config_file.close()

def location_list(request):
    '''
    Fetch move name from DB and generate static GMaps link
    '''
    try:
        # Get details from OMDb API and fetch details of locations from local PG database
        if(request.GET.get('movie_name')):
            movie_name = request.GET.get('movie_name')
            movie_info = requests.get("http://www.omdbapi.com/?t="+movie_name+"&plot=short&r=json")
            movie = Movie.objects.filter(title=movie_name).first()
        # Can be removed, no longer in use
        if(request.GET.get('id')):
            movie_id = request.GET.get('id').replace("/", "")
            movie = Movie.objects.filter(id=movie_id).first()
    except AttributeError:
        raise Http404("Movie does not exist")
    # Generate GMap link (Hack), refactor to JS on frontend when using Dynamic maps/LatLongs
    gmap = "https://maps.googleapis.com/maps/api/staticmap?center=San+Francisco&zoom=12&scale=false&size=900x600&format=png&visual_refresh=true&markers=size:mid%7Ccolor:red"
    markerlocs = ""
    try:
        locations = Location.objects.filter(movie=movie)
        for location in locations:
            markerlocs += "%7C" + location.locations + ",+San+Francisco"
        context = {
        'movie': movie,
        'movie_info': movie_info.content,
        'locations': locations,
        'maps': gmap + markerlocs + "&key=" + config['api_key']
        }
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'locations/detail.html', context)

def index(request):
    '''
    List of all movies to show up in Autocomplete textbox
    '''
    movie_list = Movie.objects.order_by('title')
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'locations/index.html', context)