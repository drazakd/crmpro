from django.urls import path
from . import views

urlpatterns = [
    path('vente', views.vente, name='vente'),
    path('ajouter_vente', views.ajouter_vente, name='ajouter_vente'),
    path('modifer_vente', views.modifier_vente, name='modifier_vente'),
    path('supprimer_vente', views.supprimer_vente, name='supprimer_vente'),

    path('ajouter_client', views.ajouter_client, name='ajouter_client'),
    path('modifier_client', views.modifier_client, name='modifier_client'),
    path('supprimer_client', views.supprimer_client, name='supprimer_client')
]