from django.urls import path
from . import views

urlpatterns = [
    path('vente', views.vente, name='vente'),
]