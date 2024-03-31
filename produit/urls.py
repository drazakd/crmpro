from django.urls import path
from . import views

urlpatterns = [
    path('produit', views.produit, name='produit'),
    path('ajouter_categorie', views.ajouter_categorie, name='ajouter_categorie'),
    path('ajouter_produit', views.ajouter_produit, name='ajouter_produit')
]