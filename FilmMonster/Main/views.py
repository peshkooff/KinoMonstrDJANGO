from django.shortcuts import render


def index(request):
    return render(request, 'layout/basic.html')


def films(request):
    return render(request, 'layout/films.html')