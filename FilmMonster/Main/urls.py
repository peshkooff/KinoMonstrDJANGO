from django.urls import path
from .views import index, films, serials, info, rating, contacts, film_content, serial_content, ChangeUserInfoView


urlpatterns = [
    path('', index, name='index'),
    path('films/', films, name='films'),
    path('serials/', serials, name='serials'),
    path('info/', info, name='info'),
    path('rating/', rating, name='rating'),
    path('contacts/', contacts, name='contacts'),
    path('films/film_content', film_content, name='film_content'),
    path('serials/serial_content', serial_content, name='serial_content'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
]