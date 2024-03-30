from django.db import models

# Create your models here.
class Vente(models.Model):
    id_vente = models.AutoField(primary_key=True)
    date_vente = models.DateTimeField()
    id = models.IntegerField(blank=True, null=True)
    id_produit = models.IntegerField(blank=True, null=True)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    id_client = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vente'


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
