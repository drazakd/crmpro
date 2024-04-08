from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


# Create your models here.

class Utilisateurs(AbstractUser):
    role = models.CharField(max_length=30, choices=[('gestionnaire', 'Gestionnaire'), ('gerant', 'Gérant')], default='M')
    gender = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    groups = models.ManyToManyField(Group, related_name='utilisateurs_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='utilisateurs_user_permissions', blank=True)




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
    utilisateurs_id = models.BigIntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_utilisateurs_groups'
        unique_together = (('utilisateurs_id', 'group_id'),)


class AccountsUtilisateursUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    utilisateurs_id = models.BigIntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_utilisateurs_user_permissions'
        unique_together = (('utilisateurs_id', 'permission_id'),)