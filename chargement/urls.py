from django.urls import path
from . import views
from .views import exporter_csv

urlpatterns = [
    path('charger', views.import_ventes_pdf, name='charger'),
    path('exporter/csv/', exporter_csv, name='exporter_csv'),
    # Autres URL de votre projet
]
