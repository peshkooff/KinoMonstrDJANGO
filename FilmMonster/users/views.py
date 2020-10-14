from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class KLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'layout/basic.html'
