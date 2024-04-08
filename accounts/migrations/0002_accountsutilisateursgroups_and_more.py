# Generated by Django 5.0.3 on 2024-04-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsUtilisateursGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('utilisateurs_id', models.BigIntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'accounts_utilisateurs_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsUtilisateursUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('utilisateurs_id', models.BigIntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'accounts_utilisateurs_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsUtilisateurs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('role', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'accounts_utilisateurs',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Utilisateurs',
        ),
    ]