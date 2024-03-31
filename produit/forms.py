from django.forms import ModelForm
from .models import Categorie
from .models import Produit

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'



class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'