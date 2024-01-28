from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def song(request):
    return render(request, "canciones.html")


def record(request):
    return render(request, "grabar.html")
