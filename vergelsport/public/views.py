from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'public/home.html')


def contacto(request):
    return render(request, 'public/contacto.html')


def servicios(request):
    return render(request, 'public/servicios.html')


def conoceme(request):
    return render(request, 'public/conoceme.html')


def opiniones(request):
    return render(request, 'public/opiniones.html')
