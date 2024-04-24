from django import forms
from django.forms import ModelForm
from .models import Fournisseur
from .models import LigneCommandeFournisseur
from .models import CommandeFournisseur
from .models import Produit
from accounts.models import AccountsUtilisateurs

class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'


# class LigneCommandeFournisseurForm(ModelForm):
#     class Meta:
#         model = LigneCommandeFournisseur
#         fields = '__all__'
#
#
#
# class CommandeFournisseurForm(ModelForm):
#     class Meta:
#         model = CommandeFournisseur
#         fields = '__all__'




class LigneCommandeFournisseurForm(ModelForm):
    class Meta:
        model = LigneCommandeFournisseur
        fields = '__all__'
        widgets = {
            'quantite_commandee': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control'}),
            'etat': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configurer le champ id_produit pour afficher les noms des produits
        self.fields['id_produit'].queryset = Produit.objects.all()
        self.fields['id_produit'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_produit'].label_from_instance = lambda obj: obj.nom

        # Configurer le champ id_commande_fournisseur pour afficher l'ID de la commande fournisseur
        self.fields['id_commande_fournisseur'].queryset = CommandeFournisseur.objects.all()
        self.fields['id_commande_fournisseur'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_commande_fournisseur'].label_from_instance = lambda \
            obj: f"Commande {obj.id_commande_fournisseur}"


class CommandeFournisseurForm(ModelForm):
    class Meta:
        model = CommandeFournisseur
        fields = '__all__'
        widgets = {
            'date_commande': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'etat': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configurer le champ id_gestionnaire pour afficher les noms des gestionnaires
        self.fields['id_gestionnaire'].queryset = AccountsUtilisateurs.objects.all()
        self.fields['id_gestionnaire'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_gestionnaire'].label_from_instance = lambda obj: obj.nom

        # Configurer le champ id_fournisseur pour afficher les noms des fournisseurs
        self.fields['id_fournisseur'].queryset = Fournisseur.objects.all()
        self.fields['id_fournisseur'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_fournisseur'].label_from_instance = lambda obj: obj.nom

