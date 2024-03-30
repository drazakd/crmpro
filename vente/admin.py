from django.contrib import admin
from .models import Vente
from .models import Client

# Register your models here.
admin.site.register(Vente)
admin.site.register(Client)
