from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification
from django.utils import timezone


user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошёл активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещания о появлении новых фильмах?')


class Movie(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='img')
    banner = models.ImageField(upload_to='img')
    category = models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'),
                                         ('drama', 'DRAMA'), ('romance', 'ROMANCE')], max_length=10)
    language = models.CharField(choices=[('english', 'ENGLISH'), ('russian', 'RUSSIAN')], max_length=10)
    producer = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    movie_trailer = models.URLField()
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)


class Serial(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='img')
    banner = models.ImageField(upload_to='img')
    category = models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'),
                                         ('drama', 'DRAMA'), ('romance', 'ROMANCE')], max_length=10)
    language = models.CharField(choices=[('english', 'ENGLISH'), ('russian', 'RUSSIAN')], max_length=10)
    producer = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    movie_trailer = models.URLField()
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)

