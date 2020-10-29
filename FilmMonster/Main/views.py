from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from .forms import LoginForm
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import AdvUser
from .forms import ChangeUserInfo
from django.contrib.auth.mixins import LoginRequiredMixin


class ChangeUserInfoView(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    model = AdvUser
    template_name = 'layout/change_user_info.html'
    form_class = ChangeUserInfo
    success_url = reverse_lazy('profile')
    success_message = 'Личные данные успешно изменены'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class FPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'layout/password_change.html'
    success_url = reverse_lazy('profile')
    success_message = 'Пароль успешно изменён!'


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