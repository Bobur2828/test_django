from django.shortcuts import render
from .models import Place
def place(request,pk):
    places=Place.objects.filter(pk=pk)
    data={
        'places': places
    }
    return render(request,'places/place.html',context=data)
