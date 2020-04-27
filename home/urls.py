from django.urls import path
from .views import landing_page, another_page

urlpatterns = [
    path('landing-page', landing_page, name="landing"),
    path('another-page', another_page),
]