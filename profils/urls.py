from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('desactiver/<int:pk>', views.desactiver_utilisateur, name='desactiver_utilisateur'),
    path('activer/<int:pk>', views.activer_utilisateur, name='activer_utilisateur')

]