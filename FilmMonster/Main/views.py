from django.shortcuts import render


def index(request):
    return render(request, 'layout/basic.html')


def films(request):
    return render(request, 'layout/films.html')


def serials(request):
    return render(request, 'layout/serials.html')


def info(request):
    return render(request, 'layout/info.html')


def raiting(request):
    return render(request, 'layout/raiting.html')