from django.forms import ModelForm
from .models import Vente, Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class VenteForm(ModelForm):
    class Meta:
        model = Vente
        fields = '__all__'
