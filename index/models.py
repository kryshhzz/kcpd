from django.db import models

# Create your models here.

import datetime


class person(models.Model):
  name = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
    return self.name
  
class genre(models.Model):
  name = models.CharField(max_length=25, unique=True)
  
  def __str__(self):
    return self.name

class lang(models.Model):
  name = models.CharField(max_length=25,unique=True)
  
  def __str__(self):
    return self.name


class film(models.Model):
  title = models.CharField(max_length = 250,unique=True)
  image = models.TextField(default="")
  image_horizontal = models.TextField(default="")
  director = models.ForeignKey(person, on_delete=models.CASCADE,related_name="director")
  release_date = models.DateField(default=datetime.date.today)
  cast = models.ManyToManyField(person)
  genres = models.ManyToManyField(genre)
  dlink = models.TextField()
  wlink = models.TextField(default="")
  tlink = models.TextField()
  rating = models.FloatField()
  language = models.ManyToManyField(lang)
  
  def __str__(self):
    return self.title