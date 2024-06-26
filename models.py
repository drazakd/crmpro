# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsUtilisateurs(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    role = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'accounts_utilisateurs'


class AccountsUtilisateursGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    accountsutilisateurs_id = models.BigIntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_utilisateurs_groups'
        unique_together = (('accountsutilisateurs_id', 'group_id'),)


class AccountsUtilisateursUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    utilisateurs_id = models.BigIntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_utilisateurs_user_permissions'
        unique_together = (('utilisateurs_id', 'permission_id'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categorie'


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


class CommandeFournisseur(models.Model):
    id_commande_fournisseur = models.AutoField(primary_key=True)
    date_commande = models.DateTimeField()
    id_gestionnaire = models.ForeignKey(AccountsUtilisateurs, models.DO_NOTHING, db_column='id_gestionnaire', blank=True, null=True)
    id_fournisseur = models.ForeignKey('Fournisseur', models.DO_NOTHING, db_column='id_fournisseur', blank=True, null=True)
    etat = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'commande_fournisseur'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoPlotlyDashDashapp(models.Model):
    instance_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    base_state = models.TextField()
    creation = models.DateTimeField()
    update = models.DateTimeField()
    save_on_change = models.IntegerField()
    stateless_app_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_dashapp'


class DjangoPlotlyDashStatelessapp(models.Model):
    app_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_statelessapp'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fournisseur(models.Model):
    id_fournisseur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    adresse = models.TextField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    telephone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fournisseur'


class LigneCommandeFournisseur(models.Model):
    id_ligne_commande_fournisseur = models.AutoField(primary_key=True)
    quantite_commandee = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    etat = models.CharField(max_length=8)
    id_commande_fournisseur = models.ForeignKey(CommandeFournisseur, models.DO_NOTHING, db_column='id_commande_fournisseur', blank=True, null=True)
    id_produit = models.ForeignKey('Produit', models.DO_NOTHING, db_column='id_produit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ligne_commande_fournisseur'


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


class Utilisateurs(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    genre = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)
    mot_de_passe = models.CharField(max_length=255)
    role = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'utilisateurs'


class Vente(models.Model):
    id_vente = models.AutoField(primary_key=True)
    date_vente = models.DateTimeField()
    id_produit = models.ForeignKey(Produit, models.DO_NOTHING, db_column='id_produit', blank=True, null=True)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_client', blank=True, null=True)
    id = models.ForeignKey(AccountsUtilisateurs, models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vente'
