from django.urls import path
from .views import index, films, serials, info, rating, contacts


urlpatterns = [
    path('', index, name='index'),
    path('films/', films, name='films'),
    path('serials/', serials, name='serials'),
    path('info/', info, name='info'),
    path('rating/', rating, name='rating'),
    path('contacts/', contacts, name='contacts'),
]