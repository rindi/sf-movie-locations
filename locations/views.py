from django.http import HttpResponse
from locations.models import Location, Movie
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
import requests
import yaml

config_file = open('static/config.yaml')
config = yaml.load(config_file)
config_file.close()


def location_list(request):
    '''
    Fetch move name from DB and generate static GMaps link
    '''
    try:
        # Get details from OMDb API and fetch details of locations from local
        # PG database
        if(request.GET.get('movie_name')):
            movie_name = request.GET.get('movie_name')
            movie_info = get_OMDb_info(movie_name)
            movie = Movie.objects.filter(title=movie_name).first()
    except AttributeError:
        raise Http404("Movie does not exist")
    try:
        locations = Location.objects.filter(movie=movie)
        context = {
            'movie': movie,
            'movie_info': movie_info.content,
            'locations': locations,
            'maps': static_map_link(locations)
        }
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'locations/detail.html', context)


def get_OMDb_info(movie_name):
    movie_info = requests.get(
        "http://www.omdbapi.com/?t=" +
        movie_name +
        "&plot=short&r=json")
    return movie_info


def static_map_link(locations):
    # Generate GMap link (Hack), refactor to JS on frontend when using Dynamic
    # maps/LatLongs
    gmap = "https://maps.googleapis.com/maps/api/staticmap?center=San+Francisco&zoom=12&scale=false&size=900x600&format=png&visual_refresh=true&markers=size:mid%7Ccolor:red"
    markerlocs = ""
    for location in locations:
        markerlocs += "%7C" + location.locations + ",+San+Francisco"
    maps = gmap + markerlocs + "&key=" + config['api_key']
    return maps


def index(request):
    '''
    List of all movies to show up in Autocomplete textbox
    '''
    movie_list = Movie.objects.order_by('title')
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'locations/index.html', context)
