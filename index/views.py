from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.utils import timezone


def index_view(request):
    films_list = film.objects.filter(title="")
    cont = {}
    current_year = timezone.now().year
    films_list = film.objects.filter(release_date__year__gte = current_year - 1).order_by("-release_date","-pk")[:10]
    sukku_list = film.objects.filter(director__name='Sukumar').order_by('-rating')
    pspk_list = film.objects.filter(cast__name='Pawan Kalyan').order_by('-rating')
    mb_list = film.objects.filter(cast__name='Mahesh Babu').order_by('-rating')
    aa_list = film.objects.filter(cast__name='Allu Arjun').order_by('-rating')
    cont = {
        "filmographies" : {
            'Latest Films' : films_list,
            "Sukumar's Brlliance" : sukku_list,
            "PSPK Filmography" : pspk_list,
            "SSMB Filmography" : mb_list,
            "AA Filmography" : aa_list,
        }
    }
    return render(request,"index.html",cont)

def search_view(request):
  if request.method == "GET":
    query = request.GET.get('query')
    films_list = film.objects.filter(title__icontains=query).order_by("-release_date","-pk")  
    return render(request,"search.html",{"films":films_list})

def detail_view(request,title):
  req_film = film.objects.filter(title=title)
  return render(request,"detail.html",{"film":req_film[0]})