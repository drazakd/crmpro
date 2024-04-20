from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Vente, Client
from .forms import VenteForm, ClientForm

# Create your views here.
def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gerant', 'admin']).exists()

@login_required
@user_passes_test(user_in_groups)
def vente(request):
    ventes = Vente.objects.all()
    clients = Client.objects.all()
    context = {'vente': ventes, 'client': clients}
    return render(request, 'vente/vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def ajouter_vente(request):
    form = VenteForm()
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def modifier_vente(request,pk):
    vente = Vente.objects.get(id_vente=pk)
    form = VenteForm(instance=vente)

    if request.method == 'POST':
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def supprimer_vente(request,pk):
    vente = VenteForm.objects.get(id_vente=pk)
    if request.method == 'POST':
        vente.delete()
        return redirect('vente')

    context = {'item': vente}
    return render(request, 'vente/supprimer_vente.html', context)


@login_required
@user_passes_test(user_in_groups)
def ajouter_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_client.html', context)


@login_required
@user_passes_test(user_in_groups)
def modifier_client(request,pk):
    client = Client.objects.get(id_client=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('vente')

    context = {'form': form}
    return render(request, 'vente/ajouter_client.html', context)


@login_required
@user_passes_test(user_in_groups)
def supprimer_client(request,pk):
    client = ClientForm.objects.get(id_client=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('vente')

    context = {'item': client}
    return render(request, 'vente/supprimer_client.html', context)