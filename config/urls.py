
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing, name='landing'),
    path('users/',include('users.urls')),
    path('place/',include('places.urls')),


    


]
