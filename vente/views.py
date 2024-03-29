from django.shortcuts import render

# Create your views here.
def vente(request):
    return render(request, 'vente/vente.html')