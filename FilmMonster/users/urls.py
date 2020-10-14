from django.urls import path
from .views import profile, KLogoutView

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('logout/', KLogoutView.as_view(), name='logout'),
]