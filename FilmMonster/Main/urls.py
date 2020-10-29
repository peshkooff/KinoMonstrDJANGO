from django.urls import path
from .views import index, films, serials, info, rating, contacts, film_content, serial_content, ChangeUserInfoView
from .views import FPasswordChangeView, RegisterUserDoneView, RegisterUserView, user_activate
urlpatterns = [
    path('', index, name='index'),
    path('films/', films, name='films'),
    path('serials/', serials, name='serials'),
    path('info/', info, name='info'),
    path('rating/', rating, name='rating'),
    path('contacts/', contacts, name='contacts'),
    path('films/film_content', film_content, name='film_content'),
    path('serials/serial_content', serial_content, name='serial_content'),
    path('accounts/profile/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/change/', FPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterUserDoneView.as_view(), name='register_done'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate')

]