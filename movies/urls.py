from django.urls import path
from .views import opening_credits, closing_credits, test_html, test_data, get_me_the_data, get_all_movies, create, read

urlpatterns = [
    path('opening-credits', opening_credits, name="opening_credits"),
    path('closing-credits', closing_credits),
    path('test-html', test_html),
    path('test-data', test_data),
    path('all-data', get_me_the_data),
    path('all-movies', get_all_movies),
    path('create', create),
    path('read', read),
]