from django.shortcuts import render
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
from produit.models import Produit
from vente.forms import Client
from vente.models import Vente


# Create your views here.
@login_required(login_url='home')
def dashboard(request):
    nombre_produits = Produit.objects.count()
    nombre_ventes = Vente.objects.count()
    nombre_clients = Client.objects.count()

    # Calculez le chiffre d'affaires total (somme de quantite * prix_unitaire)
    chiffre_affaires = Vente.objects.aggregate(
        chiffre_affaires_total= Sum(F('quantite') * F('prix_unitaire'))
    )['chiffre_affaires_total']

    # Obtenir les cinq produits les plus vendus
    top_5_produits = (
        Vente.objects
        .values('id_produit__nom')
        .annotate(total_quantite=Sum('quantite'))
        .order_by('-total_quantite')  # Trier par quantité totale vendue (décroissant)
        [:5]  # Obtenir les cinq meilleurs
    )

    # Obtenir les cinq meilleurs clients
    top_5_clients = (
        Vente.objects
        .values('id_client__nom')
        .annotate(total_depsense=Sum(F('quantite') * F('prix_unitaire')))
        .order_by('-total_depsense')  # Trier par montant total dépensé (décroissant)
        [:5]  # Obtenir les cinq meilleurs clients
    )

    context = {
        'nombre_produits':nombre_produits,
        'nombre_ventes':nombre_ventes,
        'nombre_clients':nombre_clients,
        'chiffre_affaires':chiffre_affaires,
        'top_5_produits': top_5_produits,
        'top_5_clients': top_5_clients,
    }
    return render(request, 'profils/dashboard.html', context)

@login_required(login_url='home')
def profile(request):
    return render(request, 'profils/profile.html')