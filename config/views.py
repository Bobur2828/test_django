from django.shortcuts import render
from places.models import Place
def landing(request):
    place=Place.objects.all()
    data={'place':place}
    return render(request, 'landing.html', context=data)