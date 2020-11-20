from django.shortcuts import render
import json
# Create your views here.
from django.shortcuts import render
import tmdbsimple as tmdb
import requests
from time import mktime
import time
from datetime import datetime, date
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



#API KEYS and Request Parameters
tmdb.API_KEY = '977c9fd7d952560acf0046a1cb92b01a'
DEVELOPER_KEY = 'AIzaSyCZKLBjdBQA7RIFL9uwy8z2BpDWeA0-p-s'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Create your views here.
def movies(request):
    popular_movies_tmdb = tmdb.Movies('popular')
    popular_movies = popular_movies_tmdb.info()['results']

    upcoming_movies_tmdb = tmdb.Movies('upcoming')
    upcoming_movies = upcoming_movies_tmdb.info()['results']

    return render(request, 'movies.html', {'popular':popular_movies, 'upcoming':upcoming_movies})

def single_movie(request, movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2fe5b0203afe6f89a9ad311bd55df300&append_to_response=videos')
    data = response.json()
    movies = data['videos']['results']
    
   


    return render(request, 'single_movie.html',{'videos':movies})
    