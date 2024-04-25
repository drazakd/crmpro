from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Produit, Categorie
from .forms import ProduitForm, CategorieForm

def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gestionnaire', 'admin']).exists()

@login_required
@user_passes_test(user_in_groups)
def produit(request):
    # Obtenir tous les produits et catégories
    produits = Produit.objects.all()
    categories = Categorie.objects.all()

    # Configurer la pagination
    produit_paginator = Paginator(produits, 10)  # Limiter à 10 produits par page
    categorie_paginator = Paginator(categories, 10)  # Limiter à 10 catégories par page

    # Obtenir le numéro de page de la requête pour les produits et les catégories
    produit_page_number = request.GET.get('produit_page', 1)
    categorie_page_number = request.GET.get('categorie_page', 1)

    # Obtenir les produits et catégories de la page actuelle
    produit_page = produit_paginator.get_page(produit_page_number)
    categorie_page = categorie_paginator.get_page(categorie_page_number)

    # Passez les objets paginés au template
    context = {
        'produit_page': produit_page,
        'categorie_page': categorie_page,
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
        if form.is_valid():
            form.save()
            return redirect('produit')

    context = {'form': form}
    return render(request, 'produit/ajouter_produit.html',context)


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