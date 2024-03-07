from django.urls import path

from . import views

urlpatterns = [

    path('' , views.home, name='home'),
    path('add_campanha/', views.add_campanha, name='add_campanha'),
    path('add_evento/', views.add_evento, name='add_evento'),
   
]