

from django.urls import path
from .views import place

app_name = 'place'

urlpatterns = [
    path('place/<int:pk>',place, name='place'),


    
]