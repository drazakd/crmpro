from django.db import models
from django.contrib.auth import login

# Create your models here.
class Fournisseur(models.Model):
    id_fournisseur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'fournisseur'



class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_categorie

    class Meta:
        managed = False
        db_table = 'categorie'


class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_fournisseur = models.ForeignKey(Fournisseur, models.DO_NOTHING, db_column='id_fournisseur', blank=True, null=True)
    id_categorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='id_categorie', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produit'
