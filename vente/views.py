from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Vente, Client
from .forms import VenteForm, ClientForm

# Create your views here.
def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gerant', 'admin']).exists()

@login_required
@user_passes_test(user_in_groups)
def vente(request):
    # Obtenir les choix de tri de l'utilisateur
    sort_by = request.GET.get('sort_by', 'date_vente')  # Par défaut, trier par date de vente
    order = request.GET.get('order', 'desc')  # Par défaut, ordre décroissant

    # Vérifiez que le tri est soit par date de vente, client, produit, ou prix unitaire
    if sort_by not in ['date_vente', 'id_client', 'id_produit', 'prix_unitaire']:
        sort_by = 'date_vente'  # Valeur par défaut

    # Déterminer l'ordre de tri basé sur les choix de l'utilisateur
    if order == 'asc':
        order_by = sort_by
    else:
        order_by = f'-{sort_by}'

    # Obtenir toutes les ventes triées selon les préférences de l'utilisateur
    ventes = Vente.objects.all().order_by(order_by)
    # Obtenir tous les clients
    clients = Client.objects.all()

    # Configurer la pagination pour les ventes et les clients
    vente_paginator = Paginator(ventes, 10)  # Limiter à 10 ventes par page
    client_paginator = Paginator(clients, 10)  # Limiter à 10 clients par page

    # Obtenir les numéros de page de la requête pour les ventes et les clients
    vente_page_number = request.GET.get('vente_page', 1)
    client_page_number = request.GET.get('client_page', 1)

    # Obtenir les ventes et clients de la page actuelle
    vente_page = vente_paginator.get_page(vente_page_number)
    client_page = client_paginator.get_page(client_page_number)

    # Passez les choix de tri à la vue pour les afficher dans le template
    context = {
        'vente_page': vente_page,
        'client_page': client_page,
        'sort_by': sort_by,
        'order': order,
    }

    return render(request, 'vente/vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def ajouter_vente(request):
    form = VenteForm()

    if request.method == 'POST':
        form = VenteForm(request.POST)

        if form.is_valid():
            vente = form.save(commit=False)

            # Récupérer le produit associé à la vente
            produit = vente.id_produit

            # Vérifier si le stock est suffisant pour la quantité demandée
            if produit.stock < vente.quantite:
                # Si le stock est insuffisant, afficher un message d'erreur
                messages.error(request,
                               f"Stock insuffisant pour {produit.nom}. La quantité demandée est {vente.quantite}, mais le stock disponible est {produit.stock}.")
                # Ne pas enregistrer la vente et rediriger vers le formulaire
                return render(request, 'vente/ajouter_vente.html', {'form': form})

            # Réduire le stock du produit
            produit.stock -= vente.quantite

            # Enregistrer la vente
            vente.save()

            # Enregistrer les changements au produit
            produit.save()

            # Afficher un message de succès
            messages.success(request, 'Vente effectuée avec succès.')
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def modifier_vente(request,pk):
    vente = Vente.objects.get(id_vente=pk)
    form = VenteForm(instance=vente)

    if request.method == 'POST':
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def supprimer_vente(request,pk):
    vente = VenteForm.objects.get(id_vente=pk)
    if request.method == 'POST':
        vente.delete()
        return redirect('vente')

    context = {'item': vente}
    return render(request, 'vente/supprimer_vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def ajouter_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_client.html', context)


@login_required
@user_passes_test(user_in_groups)
def modifier_client(request,pk):
    client = Client.objects.get(id_client=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_client.html', context)


@login_required
@user_passes_test(user_in_groups)
def supprimer_client(request,pk):
    client = ClientForm.objects.get(id_client=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('vente')

    context = {'item': client}
    return render(request, 'vente/supprimer_client.html', context)