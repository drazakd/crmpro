from django.urls import path
from . import views

urlpatterns = [
    path('produit', views.produit, name='produit'),
]