from django import forms
from django.forms import ModelForm
from .models import Vente, Client, Produit


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


# class VenteForm(ModelForm):
#     class Meta:
#         model = Vente
#         fields = '__all__'


class VenteForm(ModelForm):
    class Meta:
        model = Vente
        fields = ['date_vente', 'id_produit', 'quantite',  'id_client']
        widgets = {
            'date_vente': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Modifier les champs pour afficher le nom du produit et du client
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configurer le champ id_produit pour afficher les noms des produits
        self.fields['id_produit'].queryset = Produit.objects.all()
        self.fields['id_produit'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_produit'].label_from_instance = lambda obj: f"{obj.nom}"

        # Configurer le champ id_client pour afficher les noms des clients
        self.fields['id_client'].queryset = Client.objects.all()
        self.fields['id_client'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_client'].label_from_instance = lambda obj: f"{obj.nom} {obj.prenom}"