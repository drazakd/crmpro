from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CategorieForm, ProduitForm
from .models import Categorie, Produit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gestionnaire', 'admin']).exists()

@login_required
@user_passes_test(user_in_groups)
def produit(request):
    produits_list = Produit.objects.all()
    categories_list = Categorie.objects.all()

    # Créez un Paginator avec une limite de 10 éléments par page
    paginator_produits = Paginator(produits_list, 10)
    paginator_categories = Paginator(categories_list, 10)

    # Récupérez le numéro de page de la requête
    page_number = request.GET.get('page', 1)

    try:
        produits = paginator_produits.page(page_number)
        categories = paginator_categories.page(page_number)
    except PageNotAnInteger:
        # Si le numéro de page n'est pas un entier, retournez la première page
        produits = paginator_produits.page(1)
        categories = paginator_categories.page(1)
    except EmptyPage:
        # Si le numéro de page dépasse les pages disponibles, retournez la dernière page
        produits = paginator_produits.page(paginator_produits.num_pages)
        categories = paginator_categories.page(paginator_categories.num_pages)

    # Passez les objets paginés et le numéro de page actuel au template
    context = {
        'produits': produits,
        'categories': categories,
        'current_page': page_number,
        'num_pages': paginator_produits.num_pages
    }

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