from django.urls import path
from . import views

urlpatterns = [
    path('charger', views.import_ventes_pdf, name='charger'),
    # Autres URL de votre projet
]
