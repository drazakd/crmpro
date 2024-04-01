from django.db import models

# Create your models here.
class Utilisateurs(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    mot_de_passe = models.CharField(max_length=255)
    role = models.CharField(max_length=12)

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'utilisateurs'




class Fournisseur(models.Model):
    id_fournisseur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    adresse = models.TextField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    telephone = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'fournisseur'



class LigneCommandeFournisseur(models.Model):
    id_ligne_commande_fournisseur = models.AutoField(primary_key=True)
    id_commande_fournisseur = models.IntegerField(blank=True, null=True)
    id_produit = models.IntegerField(blank=True, null=True)
    quantite_commandee = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    etat = models.CharField(max_length=8)




    class Meta:
        managed = False
        db_table = 'ligne_commande_fournisseur'



class CommandeFournisseur(models.Model):
    id_commande_fournisseur = models.AutoField(primary_key=True)
    date_commande = models.DateTimeField()
    id_gestionnaire = models.ForeignKey('Utilisateurs', models.DO_NOTHING, db_column='id_gestionnaire', blank=True, null=True)
    id_fournisseur = models.ForeignKey('Fournisseur', models.DO_NOTHING, db_column='id_fournisseur', blank=True, null=True)
    etat = models.CharField(max_length=8)

    def __str__(self):
        return self.etat

    class Meta:
        managed = False
        db_table = 'commande_fournisseur'


