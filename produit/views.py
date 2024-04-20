from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CategorieForm, ProduitForm
from .models import Categorie, Produit


# Create your views here.
def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gestionnaire', 'admin']).exists()

@login_required
@user_passes_test(user_in_groups)
def produit(request):

    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    context = {'produits': produits, 'categories': categories}
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