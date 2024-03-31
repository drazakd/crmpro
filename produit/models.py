from django.db import models

# Create your models here.
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
    id_fournisseur = models.IntegerField(blank=True, null=True)
    id_categorie = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'produit'



class Fournisseur(models.Model):
    id_fournisseur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'fournisseur'

