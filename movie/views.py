from django.shortcuts import render
from .models import Movies
# Create your views here.

def indexs(request):
    moviek = Movies.objects.all()
    return render(request, 'index.html', {'moviek': moviek})


def contact(request):
    return render(request, 'contact.html')

def result(request):
   
    return render(request,  'add.html')
    