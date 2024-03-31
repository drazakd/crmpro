from django.shortcuts import render, redirect
from .forms import CategorieForm, ProduitForm
from produit.models import Categorie, Produit
# Create your views here.
def produit(request):

    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    context = {'produits': produits, 'categories': categories}
    return render(request, 'produit/produit.html', context)

def ajouter_categorie(request):
    form = CategorieForm()
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    context = {'form': form}
    return render(request, 'produit/ajouter_categorie.html', context)

def ajouter_produit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    context = {'form': form}
    return render(request, 'produit/ajouter_produit.html',context)
