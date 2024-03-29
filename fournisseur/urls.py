from django.urls import path
from . import views

urlpatterns = [
    path('fournisseur', views.fournisseur, name='fournisseur'),
]