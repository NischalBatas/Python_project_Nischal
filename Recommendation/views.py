from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'help.html', {'name': 'Nishma'})

def subtract(request):
    n1= int(request.GET['num1'])
    n2= int(request.GET['num2'])
    n3= n1-n2
    return render(request, 'add.html',{'result': n3})

def help(request):
    e1= int(request.POST['n1'])
    e2=int(request.POST['n2'])
    e3=e1+e2

    return render(request, 'add.html', {'mark':e3})