from django.db import models
from tastypie.resources import ModelResource
from myapp.models import Movies


class MovieResource(ModelResource):
    class Meta:
        queryset = Movies.objects.all()

        resource_name= 'data'
