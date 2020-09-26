from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def home(request):
    movie=Movies.objects.all()

    return render(request,'myapp/home_page.html',{'movies':movie})


