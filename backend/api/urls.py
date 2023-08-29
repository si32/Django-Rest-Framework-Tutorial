from django.urls import path

from .views import api_home


urlpatterns = [
    path('', api_home, name='api_home') # http://localhost:8000/api/
]
