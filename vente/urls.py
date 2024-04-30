from django.urls import path
from . import views

urlpatterns = [
    path('vente', views.vente, name='vente'),
    path('ajouter_vente', views.ajouter_vente, name='ajouter_vente'),
    path('modifer_vente/<int:pk>', views.modifier_vente, name='modifier_vente'),
    path('supprimer_vente/<int:pk>', views.supprimer_vente, name='supprimer_vente'),

    path('ajouter_client', views.ajouter_client, name='ajouter_client'),
    path('modifier_client/<int:pk>', views.modifier_client, name='modifier_client'),
    path('supprimer_client/<int:pk>', views.supprimer_client, name='supprimer_client')
]