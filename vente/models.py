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

    # Méthode save pour mettre à jour le prix unitaire
    def save(self, *args, **kwargs):
        # Si un produit est sélectionné
        if self.id_produit:
            # Obtenez le prix du produit sélectionné
            produit = self.id_produit
            # Mettez à jour le champ prix_unitaire avec le prix du produit
            self.prix_unitaire = produit.prix

        # Appelez la méthode save de la classe parente
        super().save(*args, **kwargs)



    # Méthode pour calculer le montant total de la vente
    @property
    def montant_total(self):
        return self.prix_unitaire * self.quantite
