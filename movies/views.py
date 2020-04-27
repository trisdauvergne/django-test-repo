from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def opening_credits(request):
    return HttpResponse('Welcome to this movie lol!')


def closing_credits(request):
    return HttpResponse('Bye hope you enjoyed it.')


def test_html(request):
    return render(request, 'movies/home.html')


def test_data(request):
    movie = {'title': 'Titanic',
             'synopsys': 'A movie about a ship',
             'release': 'The 90s'}
    return render(request, 'movies/home.html', movie)


def get_me_the_data(request):
    data = {'movies': [
                       {'title': 'Avatar',
                        'synopsys': 'CGI movie with blue tall people',
                        'release': 'The 00s'},
                       {'title': 'The Matrix',
                        'synopsys': 'Trippy movie',
                        'release': 'The 00s'}]}
    return render(request, 'movies/all_data.html', data)


def get_all_movies(request):
    movies = Movie.objects.all()

    data = {'movies': movies}

    return render(request, 'movies/all_movies.html', data)


def create(request):

    movie = Movie(title="My movie", synopsys="Something there", release_year="1998", duration=200)

    data = {'movie': movie}

    return render(request, 'movies/create.html', data)


def read(request):

    movie = Movie.object.all()
    data = {'movie': movie}

    return render(request, 'movies/read.html', data)