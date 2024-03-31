from django.shortcuts import render
from produit.models import Categorie, Produit
# Create your views here.
def produit(request):

    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    context = {'produits': produits, 'categories': categories}
    return render(request, 'produit/produit.html', context)