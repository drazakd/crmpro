from django.shortcuts import render

# Create your views here.
def produit(request):
    return render(request, 'produit/produit.html')