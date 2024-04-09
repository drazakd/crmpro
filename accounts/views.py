from datetime import datetime  # Importez datetime de manière appropriée
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from .models import AccountsUtilisateurs

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = AccountsUtilisateurs.objects.filter(email=email).first()
        if user:
            if check_password(password, user.password):
                login(request, user)
                return redirect('dashboard')
            else:
                print("Mot de passe incorrect")
        else:
            print("Utilisateur n'existe pas")

    return render(request, 'accounts/sign-in.html', {})


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

        # vérifier l'e-mail
        try:
            validate_email(email)
        except:
            error = True
            message = "Entrez un e-mail valide"

        # vérifier s'il existe déjà
        if AccountsUtilisateurs.objects.filter(username=username).exists() or AccountsUtilisateurs.objects.filter(email=email).exists():
            error = True
            message = f"L'e-mail {email} ou le nom d'utilisateur {username} existe déjà !"

        # enregistrement dans la bd
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
                date_joined=datetime.now(),# Utilisez datetime.now() pour obtenir l'heure actuelle
                password= hashed_password
            )
            utilisateur.save()
            return redirect('signup')  # Rediriger vers une autre vue après l'inscription

    context = {'error': error, 'message': message}
    return render(request, 'accounts/signup.html', context)
