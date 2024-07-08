from django.urls import path
from . import views


urlpatterns = [
    path('', views.nav, name='nav'),
]




# https://www.w3schools.com/django/django_slug_field.php
#
#https://www.aparat.com/v/s64zt30