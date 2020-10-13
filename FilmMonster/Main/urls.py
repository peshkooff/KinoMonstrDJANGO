from django.urls import path
from .views import index, films, serials, info, raiting


urlpatterns = [
    path('', index, name='index'),
    path('films/', films, name='films'),
    path('serials/', serials, name='serials'),
    path('info/', info, name='info'),
    path('raiting/', raiting, name='raiting'),
]