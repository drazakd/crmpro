from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
from produit.models import Produit
from vente.forms import Client
from vente.models import Vente
from accounts.models import AccountsUtilisateurs


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
    # Obtenir les années disponibles pour la sélection
    annees_disponibles = Vente.objects.dates('date_vente', 'year')
    annees_disponibles = [date.year for date in annees_disponibles]

    # Obtenir les années sélectionnées par l'utilisateur
    annees_selectionnees = request.GET.getlist('annees', annees_disponibles)

    # Obtenir les ventes par mois pour les années sélectionnées
    ventes_par_mois = (
        Vente.objects.filter(date_vente__year__in=annees_selectionnees)
        .values('date_vente__year', 'date_vente__month')
        .annotate(total_ventes=Sum('quantite'))
        .order_by('date_vente__year', 'date_vente__month')
    )

    # Préparer les données pour le graphique
    data = {}
    for vente in ventes_par_mois:
        annee = vente['date_vente__year']
        mois = vente['date_vente__month']
        total = vente['total_ventes']
        if annee not in data:
            data[annee] = [0] * 12  # Initialiser une liste de 12 mois pour l'année
        data[annee][mois - 1] = total  # Remplir les ventes pour le mois spécifique

    context = {
        'nombre_produits':nombre_produits,
        'nombre_ventes':nombre_ventes,
        'nombre_clients':nombre_clients,
        'chiffre_affaires':chiffre_affaires,
        'top_5_produits': top_5_produits,
        'top_5_clients': top_5_clients,
        # Ajouter les étiquettes et les données au contexte
        'annees_disponibles': annees_disponibles,
        'data': data,
    }
    return render(request, 'profils/dashboard.html', context)

@login_required(login_url='home')
def profile(request):
    gerants = AccountsUtilisateurs.objects.filter(role ='gerant')
    gestionnaire = AccountsUtilisateurs.objects.filter(role = "gestionnaire")
    admin = AccountsUtilisateurs.objects.filter(role= "admin")

    # Configurer la pagination
    admin_paginator = Paginator(admin, 10)  # Limiter à 10 produits par page
    gestionnaire_paginator = Paginator(gestionnaire, 10)  # Limiter à 10 catégories par page
    gerants_paginator = Paginator(gerants, 10)  # Limiter à 10 catégories par page

    # Obtenir le numéro de page de la requête pour les produits et les catégories
    admin_page_number = request.GET.get('admin_paginator', 1)
    gestionnaire_page_number = request.GET.get('gestionnaire_paginator', 1)
    gerants_page_number = request.GET.get('gerants_paginator', 1)

    # Obtenir les produits et catégories de la page actuelle
    admin_page = admin_paginator.get_page(admin_page_number)
    gestionnaire_page = gestionnaire_paginator.get_page(gestionnaire_page_number)
    gerants_page = gerants_paginator.get_page(gerants_page_number)

    # Passez les objets paginés au template
    context = {
        'admin_page': admin_page,
        'gestionnaire_page': gestionnaire_page,
        'gerants_page': gerants_page,

    }
    return render(request, 'profils/profile.html', context)


@login_required
def desactiver_utilisateur(request, pk):
    # Récupérez l'utilisateur à désactiver
    utilisateur = AccountsUtilisateurs.objects.get(id=pk)
    # Désactivez l'utilisateur en définissant is_active à False
    utilisateur.is_active = False
    # Sauvegardez les modifications
    utilisateur.save()
    # Redirigez vers une autre vue après la désactivation
    # Par exemple, vous pourriez rediriger vers la vue profile
    return redirect('profile')


@login_required
def activer_utilisateur(request, pk):
    # Récupérez l'utilisateur à désactiver
    utilisateur = AccountsUtilisateurs.objects.get(id=pk)
    # Désactivez l'utilisateur en définissant is_active à False
    utilisateur.is_active = True
    # Sauvegardez les modifications
    utilisateur.save()
    # Redirigez vers une autre vue après la désactivation
    # Par exemple, vous pourriez rediriger vers la vue profile
    return redirect('profile')

# @login_required
# @user_passes_test(user_in_groups)
# def supprimer_profils(request,pk):
#     profile = AccountsUtilisateurs.objects.get(id=pk)
#     if request.method == 'POST':
#         profile.delete()
#         return redirect('produit')
#
#     context = {'item': profile}
#     return render(request, 'profils/supprimer_profils.html', context)