from django.http import HttpResponse
from locations.models import Location, Movie
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import MovieForm

def location_list(request):
    movie_id = request.GET.get('id')
    print movie_id
    try:
        movie = Movie.objects.filter(id=movie_id).first()
        locations = Location.objects.filter(movie=movie)
        context = {
        'movie': movie,
        'locations': locations
        }
        # print movie.title
        # print locations[0].locations
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