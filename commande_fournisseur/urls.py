from django.urls import path
from . import views

urlpatterns = [
    path('commande_fournisseur', views.commande_fournisseur, name='commande_fournisseur'),
]