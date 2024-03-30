from django.contrib import admin
from .models import Fournisseur
from .models import CommandeFournisseur
from .models import LigneCommandeFournisseur

# Register your models here.
admin.site.register(Fournisseur)
admin.site.register(CommandeFournisseur)
admin.site.register(LigneCommandeFournisseur)