from django.forms import ModelForm
from .models import Fournisseur
from .models import LigneCommandeFournisseur
from .models import CommandeFournisseur


class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'


class LigneCommandeFournisseurForm(ModelForm):
    class Meta:
        model = LigneCommandeFournisseur
        fields = '__all__'



class CommandeFournisseurForm(ModelForm):
    class Meta:
        model = CommandeFournisseur
        fields = '__all__'
