from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class AccountsUtilisateursManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given username, email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username__exact=username)

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
    REQUIRED_FIELDS = [
        'email']  # Ajoutez ici d'autres champs requis pour la création d'un nouvel utilisateur, comme le courriel
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    @property
    def is_anonymous(self):
        return False  # Retourne False si l'utilisateur n'est pas anonyme

    @property
    def is_authenticated(self):
        return True  # Retourne True si l'utilisateur est authentifié


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