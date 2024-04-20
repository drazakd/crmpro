from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, Permission, Group, PermissionsMixin
from datetime import datetime

from django.utils import timezone


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
        # Assurez-vous que nis_active est défini à True par défaut
        user.is_active = True
        # Assurez-vous que date_joined est défini à la date et l'heure actuelles
        user.date_joined = datetime.now()

        user.save(using=self._db)

        # Ajouter l'utilisateur au groupe 'gestionnaire' ou 'gérant' en fonction de son rôle
        role = extra_fields.get('role')
        if role == 'gestionnaire':
            # Obtenez ou créez le groupe 'gestionnaire'
            gestionnaire_group, created = Group.objects.get_or_create(name='gestionnaire')
            # Ajoutez l'utilisateur au groupe 'gestionnaire'
            user.groups.add(gestionnaire_group)
        elif role == 'gerant':
            # Obtenez ou créez le groupe 'gérant'
            gerant_group, created = Group.objects.get_or_create(name='gerant')
            # Ajoutez l'utilisateur au groupe 'gérant'
            user.groups.add(gerant_group)
        elif role == 'admin':
            # Obtenez ou créez le groupe 'admin'
            admin_group, created = Group.objects.get_or_create(name='admin')
            # Ajoutez l'utilisateur au groupe 'admin'
            user.groups.add(admin_group)

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


# class Utilisateurs(AbstractUser, PermissionsMixin):
#     role = models.CharField(max_length=30, choices=[('gestionnaire', 'Gestionnaire'), ('gerant', 'Gérant')], default='M')
#     gender = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
#     groups = models.ManyToManyField(Group, related_name='utilisateurs_groups', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='utilisateurs_user_permissions', blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)


class AccountsUtilisateursManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("Le nom d'utilisateur doit être défini")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.date_joined = timezone.now()

        user.save(using=self._db)

        # Ajouter l'utilisateur au groupe approprié en fonction de son rôle
        role = extra_fields.get('role')
        if role == 'gestionnaire':
            group, created = Group.objects.get_or_create(name='gestionnaire')
            user.groups.add(group)
        elif role == 'gerant':
            group, created = Group.objects.get_or_create(name='gerant')
            user.groups.add(group)
        elif role == 'admin':
            group, created = Group.objects.get_or_create(name='admin')
            user.groups.add(group)

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class AccountsUtilisateurs(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)

    groups = models.ManyToManyField(Group, related_name='accounts_utilisateurs', blank=True)

    objects = AccountsUtilisateursManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return super().has_perm(perm, obj)

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    class Meta:
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