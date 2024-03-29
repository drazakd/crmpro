from django.shortcuts import render

# Create your views here.
def fournisseur(request):
    return render(request, 'fournisseur/fournisseur.html')