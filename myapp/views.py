from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from django.db.models import Q
from django.views.generic import ListView



def home(request):
    movie=Movies.objects.all()

    return render(request,'myapp/home_page.html',{'movies':movie})


class MovieListVies(ListView):
    model = Movies
    template_name = 'myapp/home_page.html'
    context_object_name = 'movies'
    paginate_by = 4
    ordering = ['release']


def search(request):
    query = request.GET.get('query')
    movie= Movies.objects.filter(Q(title__icontains=query))

    context={

        'movies':movie
    }
    return render(request,'myapp/search.html',context)








