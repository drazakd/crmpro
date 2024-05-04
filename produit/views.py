from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Produit, Categorie
from .forms import ProduitForm, CategorieForm
from produit.filters import ProduitFilter

def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gestionnaire', 'admin']).exists()

@login_required
@user_passes_test(user_in_groups)
def produit(request):
    # Obtenir les choix de tri de l'utilisateur
    sort_by = request.GET.get('sort_by', 'id_produit')  # Par défaut, trier par id_produit
    order = request.GET.get('order', 'desc')  # Par défaut, ordre décroissant

    # Vérifiez que le tri est soit par id_produit (ordre d'ajout), soit par nom, soit par prix
    if sort_by not in ['id_produit', 'nom', 'prix']:
        sort_by = 'id_produit'  # Valeur par défaut

    # Déterminer l'ordre de tri basé sur les choix de l'utilisateur
    if order == 'asc':
        order_by = sort_by
    else:
        order_by = f'-{sort_by}'

    # Obtenir tous les produits triés selon les préférences de l'utilisateur
    produits = Produit.objects.all().order_by(order_by)
    # Obtenir toutes les catégories
    categories = Categorie.objects.all()

    myFilter = ProduitFilter()

    # Configurer la pagination pour les produits et les catégories
    produit_paginator = Paginator(produits, 10)  # Limiter à 10 produits par page
    categorie_paginator = Paginator(categories, 10)  # Limiter à 10 catégories par page

    # Obtenir les numéros de page de la requête pour les produits et les catégories
    produit_page_number = request.GET.get('produit_page', 1)
    categorie_page_number = request.GET.get('categorie_page', 1)

    # Obtenir les produits et catégories de la page actuelle
    produit_page = produit_paginator.get_page(produit_page_number)
    categorie_page = categorie_paginator.get_page(categorie_page_number)

    # Passez les choix de tri à la vue pour les afficher dans le template
    context = {
        'produit_page': produit_page,
        'categorie_page': categorie_page,
        'sort_by': sort_by,
        'order': order,
        'myFilter': myFilter,
    }

    return render(request, 'produit/produit.html', context)





@login_required
@user_passes_test(user_in_groups)
def ajouter_categorie(request):
    form = CategorieForm()
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit')

    context = {'form': form}
    return render(request, 'produit/ajouter_categorie.html', context)

@login_required
@user_passes_test(user_in_groups)
def modifier_categorie(request,pk):
    categorie = Categorie.objects.get(id_categorie=pk)
    form = CategorieForm()

    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('produit')

    context = {'form':form}
    return render(request, 'produit/ajouter_categorie.html', context)

@login_required
@user_passes_test(user_in_groups)
def supprimer_categorie(request,pk):
    categorie = Categorie.objects.get(id_categorie=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('produit')

    context = {'item': categorie}
    return render(request, 'produit/supprimer_categorie.html', context)


@login_required
@user_passes_test(user_in_groups)
def ajouter_produit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)

        # Vérifiez si le produit existe déjà
        if form.is_valid():
            nom_produit = form.cleaned_data.get('nom')
            quantite_ajoutee = form.cleaned_data.get('stock')

            try:
                # Vérifiez s'il existe un produit avec le même nom
                produit = Produit.objects.get(nom=nom_produit)

                # Si le produit existe, ajoutez la quantité au stock existant
                produit.stock += quantite_ajoutee
                produit.save()

            except Produit.DoesNotExist:
                # Si le produit n'existe pas, enregistrez le nouveau produit
                form.save()

            return redirect('produit')

    context = {'form': form}
    return render(request, 'produit/ajouter_produit.html', context)


@login_required
@user_passes_test(user_in_groups)
def modifier_produit(request,pk):
    produit = Produit.objects.get(id_produit=pk)
    form = ProduitForm(instance=produit)

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit')

    context = {'form': form}
    return render(request, 'produit/ajouter_produit.html', context)

@login_required
@user_passes_test(user_in_groups)
def supprimer_produit(request,pk):
    produit = Produit.objects.get(id_produit=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('produit')

    context = {'item': produit}
    return render(request, 'produit/supprimer_produit.html', context)