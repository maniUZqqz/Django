from django.urls import path
from . import views

urlpatterns = [
    path('<day>/templates/', views.Templates, name='templates'),
    path('day/meno/', views.list_day, name='meno'),
    path('<int:day>/', views.to_day_number),
    path('<str:day>/', views.to_day, name='Number'),
    path('t/text/', views.text, name='text'),
    path('t/after_text/', views.after_text, name='after_text'),
]
