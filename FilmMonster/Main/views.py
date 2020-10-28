from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'layout/basic.html')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'layout/basic.html', {'form': form})


def films(request):
    return render(request, 'layout/films.html')


def serials(request):
    return render(request, 'layout/serials.html')


def info(request):
    return render(request, 'layout/info.html')


def rating(request):
    return render(request, 'layout/rating.html')


def contacts(request):
    return render(request, 'layout/contacts.html')


def film_content(request):
    return render(request, 'layout/film_content.html')


def serial_content(request):
    return render(request, 'layout/serial_content.html')