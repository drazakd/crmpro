from django.db import models
from django.utils import timezone

from produit.models import Produit
from accounts.models import AccountsUtilisateurs


# Create your models here.
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.TextField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    telephone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'client'



class Vente(models.Model):
    id_vente = models.AutoField(primary_key=True)
    date_vente = models.DateTimeField(default=timezone.now)
    id_produit = models.ForeignKey(Produit, models.DO_NOTHING, db_column='id_produit', blank=True, null=True)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_client', blank=True, null=True)
    id = models.ForeignKey(AccountsUtilisateurs, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'vente'

