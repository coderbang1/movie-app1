from django.urls import path
from .views import MovieListVies
from . import views



urlpatterns = [
    path('',MovieListVies.as_view(),name='home-page'),
    path('search/',views.search,name='home-query')

]
