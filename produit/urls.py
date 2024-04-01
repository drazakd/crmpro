from django.urls import path
from . import views

urlpatterns = [
    path('produit', views.produit, name='produit'),
    path('ajouter_categorie', views.ajouter_categorie, name='ajouter_categorie'),
    path('modifier_categorie/<str:pk>', views.modifier_categorie, name='modifier_categorie'),
    path('supprimer_categorie/<str:pk>', views.supprimer_categorie, name='supprimer_categorie'),

    path('ajouter_produit', views.ajouter_produit, name='ajouter_produit'),
    path('modifier_produit/<str:pk>', views.modifier_produit, name='modifier_produit'),
    path('supprimer_produit/<str:pk>', views.supprimer_produit, name='supprimer_produit')
]

