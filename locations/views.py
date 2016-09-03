from django.http import HttpResponse
from locations.models import Location, Movie
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import MovieForm

def location_list(request):
    try:
        if(request.GET.get('movie_name')):
            movie_name = request.GET.get('movie_name')
            movie = Movie.objects.filter(title=movie_name).first()
        if(request.GET.get('id')):
            movie_id = request.GET.get('id').replace("/", "")
            movie = Movie.objects.filter(id=movie_id).first()
    except AttributeError:
        raise Http404("Movie does not exist")
    gmap = "https://maps.googleapis.com/maps/api/staticmap?center=San+Francisco&zoom=12&scale=false&size=900x600&format=png&visual_refresh=true&markers=size:mid%7Ccolor:red"
    markerlocs = ""
    try:
        locations = Location.objects.filter(movie=movie)
        for location in locations:
            markerlocs += "%7C" + location.locations + ",+San+Francisco"
        context = {
        'movie': movie,
        'locations': locations,
        'maps': gmap + markerlocs
        }
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'locations/detail.html', context)

def index(request):
    movie_list = Movie.objects.order_by('title')
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'locations/index.html', context)

    # return HttpResponse(template.render(context, request))

    # output = '<li>'.join([m.title for m in movie_list])
    # return HttpResponse(output)