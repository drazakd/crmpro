from django.shortcuts import render

# Create your views here.
def commande_fournisseur(request):
    return render(request, 'commande_fournisseur/commande_fournisseur.html'),