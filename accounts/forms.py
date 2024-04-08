from django import forms
from .models import Utilisateurs

class UtilisateursForm(forms.ModelForm):
    class Meta:
        model = Utilisateurs
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role', 'gender']