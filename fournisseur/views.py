from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from fournisseur.models import Fournisseur, LigneCommandeFournisseur, CommandeFournisseur
from .forms import FournisseurForm, LigneCommandeFournisseurForm, CommandeFournisseurForm

# Create your views here.
def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gestionnaire', 'admin']).exists()

@login_required
@user_passes_test(user_in_groups)
def fournisseur(request):

    fournisseurs = Fournisseur.objects.all()
    ligne_fournisseur = LigneCommandeFournisseur.objects.all()
    commandes = CommandeFournisseur.objects.all()
    context = {'fournisseurs':fournisseurs, 'ligne_fournisseur':ligne_fournisseur, 'commandes':commandes}
    return render(request, 'fournisseur/fournisseur.html',context)

@login_required
@user_passes_test(user_in_groups)
def ajouter_fournisseur(request):
    form = FournisseurForm()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fournisseur')

    context = {'form': form}
    return render(request, 'fournisseur/ajouter_fournisseur.html', context)

@login_required
@user_passes_test(user_in_groups)
def modifier_fournisseur(request,pk):
    fournisseur = Fournisseur.objects.get(id_fournisseur=pk)
    form = FournisseurForm(instance=fournisseur)

    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('fournisseur')

    context = {'form': form}
    return render(request, 'fournisseur/ajouter_fournisseur.html', context)

@login_required
@user_passes_test(user_in_groups)
def supprimer_fournisseur(request,pk):
    fournisseur = Fournisseur.objects.get(id_fournisseur=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseur')

    context = {'item': fournisseur}
    return render(request, 'fournisseur/supprimer_fournisseur.html', context)


@login_required
@user_passes_test(user_in_groups)
def ajouter_lignecommande(request):
    form = LigneCommandeFournisseurForm()
    if request.method == 'POST':
        form = LigneCommandeFournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fournisseur')

    context = {'form': form}
    return render(request, 'fournisseur/ajouter_lignecommande.html', context)


@login_required
@user_passes_test(user_in_groups)
def modifier_lignecommande(request,pk):
    lignecommande = LigneCommandeFournisseur.objects.get(id_ligne_commande_fournisseur=pk)
    form = LigneCommandeFournisseurForm(instance=lignecommande)

    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=lignecommande)
        if form.is_valid():
            form.save()
            return redirect('fournisseur')

    context = {'form': form}
    return render(request, 'fournisseur/ajouter_fournisseur.html', context)

@login_required
@user_passes_test(user_in_groups)
def supprimer_lignecommande(request,pk):
    lignecommande = LigneCommandeFournisseur.objects.get(id_ligne_commande_fournisseur=pk)
    if request.method == 'POST':
        lignecommande.delete()
        return redirect('fournisseur')

    context = {'item': lignecommande}
    return render(request, 'fournisseur/supprimer_lignecommande.html', context)



@login_required
@user_passes_test(user_in_groups)
def ajouter_commande(request):
    form = CommandeFournisseurForm()
    if request.method == 'POST':
        form = CommandeFournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fournisseur')

    context = {'form': form}
    return render(request, 'fournisseur/ajouter_commande.html', context)

@login_required
@user_passes_test(user_in_groups)
def modifier_commande(request,pk):
    commande = CommandeFournisseur.objects.get(id_commande_fournisseur=pk)
    form = CommandeFournisseurForm(instance=commande)

    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('fournisseur')

    context = {'form': form}
    return render(request, 'fournisseur/ajouter_fournisseur.html', context)


@login_required
@user_passes_test(user_in_groups)
def supprimer_commande(request,pk):
    commande = CommandeFournisseur.objects.get(id_commande_fournisseur=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('fournisseur')

    context = {'item': commande}
    return render(request, 'fournisseur/supprimer_commande.html', context)
