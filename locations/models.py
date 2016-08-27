from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=800)
    release_year = models.PositiveSmallIntegerField()
    production_company = models.CharField(max_length=700, null=True, blank=True)
    distributor = models.CharField(max_length=700, null=True, blank=True)
    director = models.CharField(max_length=700, null=True, blank=True)
    writer = models.CharField(max_length=700, null=True, blank=True)
    actor1 = models.CharField(max_length=700, null=True, blank=True)
    actor2 = models.CharField(max_length=700, null=True, blank=True)
    actor3 = models.CharField(max_length=700, null=True, blank=True)
    
class Location(models.Model):
    locations = models.CharField(max_length=800)
    fun_facts = models.CharField(max_length=1000, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
