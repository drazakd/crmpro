from django.shortcuts import render
from fournisseur.models import Fournisseur, LigneCommandeFournisseur, CommandeFournisseur


# Create your views here.
def fournisseur(request):

    fournisseurs = Fournisseur.objects.all()
    ligne_fournisseur = LigneCommandeFournisseur.objects.all()
    commandes = CommandeFournisseur.objects.all()
    context = {'fournisseurs':fournisseurs, 'ligne_fournisseur':ligne_fournisseur, 'commandes':commandes}
    return render(request, 'fournisseur/fournisseur.html',context)