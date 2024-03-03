from django.urls import path
from .views import donation_view

app_name = 'donations'

urlpatterns = [
    path('doar/', donation_view, name='doar'),
]



