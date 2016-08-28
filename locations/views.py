from django.http import HttpResponse
from locations.models import Location, Movie
from django.template import loader
from django.shortcuts import render

def index(request):
    movie_list = Movie.objects.order_by('title')
    template = loader.get_template('locations/index.html')    
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'locations/index.html', context)

    # return HttpResponse(template.render(context, request))

    # output = '<li>'.join([m.title for m in movie_list])
    # return HttpResponse(output)