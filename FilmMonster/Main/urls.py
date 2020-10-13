from django.urls import path
from .views import index, films


urlpatterns = [
    path('', index, name='index'),
    path('films/', films, name='films'),
]