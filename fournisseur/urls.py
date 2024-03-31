from django.urls import path
from . import views

urlpatterns = [
    path('fournisseur', views.fournisseur, name='fournisseur'),
    path('ajouter_fournisseur', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('modifier_fournisseur/<str:pk>', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('supprimer_fournisseur/<str:pk>',views.supprimer_fournisseur, name='supprimer_fournisseur'),

    path('ajouter_lignecommande', views.ajouter_lignecommande, name='ajouter_lignecommande'),
    path('modifier_lignecommande/<str:pk>', views.modifier_lignecommande, name='modifier_lignecommande'),
    path('supprimer_lignecommande/<str:pk>', views.supprimer_lignecommande, name='supprimer_lignecommande'),

    path('ajouter_commande', views.ajouter_commande, name='ajouter_commande'),
    path('modifier_commande/<str:pk>', views.modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<str:pk>', views.supprimer_commande, name='supprimer_commande')
]