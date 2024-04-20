from datetime import datetime  # Importez datetime de manière appropriée
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from .models import AccountsUtilisateurs
from django.contrib.auth.models import Group


def user_in_groups(user):
    """Vérifie si l'utilisateur appartient aux groupes 'gestionnaire' ou 'admin'."""
    return user.groups.filter(name__in=['gestionnaire', 'admin']).exists()


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None

        user = AccountsUtilisateurs.objects.filter(email=email).first()
        if user:
            if check_password(password, user.password):
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Mot de passe incorrect"
        else:
            error_message = "Utilisateur n'existe pas"

        # Affichez le message d'erreur (le cas échéant)
        if error_message:
            context = {'error_message': error_message}
            return render(request, 'accounts/sign-in.html', context)

    return render(request, 'accounts/sign-in.html', {})


@login_required
@user_passes_test(user_in_groups)
def signup(request):
    error = False
    message = ""
    if request.method == 'POST':
        nom = request.POST.get('nom', None)
        prenom = request.POST.get('prenom', None)
        genre = request.POST.get('genre', None)
        role = request.POST.get('role', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        # Vérifier l'e-mail
        try:
            validate_email(email)
        except:
            error = True
            message = "Entrez un e-mail valide"

        # Vérifier si l'utilisateur existe déjà
        if AccountsUtilisateurs.objects.filter(username=username).exists() or AccountsUtilisateurs.objects.filter(
                email=email).exists():
            error = True
            message = f"L'e-mail {email} ou le nom d'utilisateur {username} existe déjà !"

        # Enregistrement dans la base de données
        if not error:
            hashed_password = make_password(password)
            utilisateur = AccountsUtilisateurs.objects.create(
                username=username,
                email=email,
                first_name=prenom,
                last_name=nom,
                gender=genre,
                role=role,
                is_active=True,
                is_superuser=False,
                is_staff=False,
                date_joined=datetime.now(),  # Utilisez datetime.now() pour obtenir l'heure actuelle
                password=hashed_password
            )

            # Ajoutez l'utilisateur au groupe approprié en fonction de son rôle
            if role == 'gestionnaire':
                # Obtenez ou créez le groupe 'gestionnaire'
                gestionnaire_group, created = Group.objects.get_or_create(name='gestionnaire')
                utilisateur.groups.add(gestionnaire_group)
            elif role == 'gerant':
                # Obtenez ou créez le groupe 'gerant'
                gerant_group, created = Group.objects.get_or_create(name='gerant')
                utilisateur.groups.add(gerant_group)
            elif role == 'admin':
                # Obtenez ou créez le groupe 'admin'
                admin_group, created = Group.objects.get_or_create(name='admin')
                utilisateur.groups.add(admin_group)

            utilisateur.save()
            return redirect('signup')  # Redirige vers une autre vue après l'inscription

    context = {'error': error, 'message': message}
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
