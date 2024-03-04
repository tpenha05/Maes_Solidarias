from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add_produto, name='add_produto')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)