from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from produit.models import Produit
from vente.models import Client, Vente
from fournisseur.models import Categorie  # Remplacez les noms des modèles si nécessaire
import tabula
import pandas as pd
import numpy as np

# Vue pour importer les ventes à partir d'un fichier PDF
from django.http import request



# Vue pour importer les ventes à partir d'un fichier PDF
def import_ventes_pdf(request):
    if request.method == 'POST':
        # Vérifiez si un fichier a été soumis
        if 'fichier' not in request.FILES:
            messages.error(request, 'Aucun fichier sélectionné.')
            return redirect('charger')

        # Récupérer le fichier téléchargé
        fichier_obj = request.FILES['fichier']

        # Lire les données du PDF
        dfs = tabula.read_pdf(fichier_obj, pages='all', multiple_tables=True, encoding='latin-1')

        # Nettoyer les noms de colonnes
        dfs_propres = []
        for df in dfs:
            df.columns = [col.strip().replace(" ", "") for col in df.columns]
            dfs_propres.append(df)

        # Concaténer les DataFrames de chaque page en un seul DataFrame
        df_concat = pd.concat(dfs_propres, ignore_index=True)

        # Renommer les colonnes selon votre PDF
        df_concat.columns = ["id", "Name", "Gender", "Produit", "Type", "Prix", "Date"]

        # Remplacer les valeurs NaN par des chaînes vides
        df_concat.replace({np.nan: ""}, inplace=True)

        # Insérer les données dans les tables de base de données
        for index, row in df_concat.iterrows():
            # Obtenir la catégorie (vérifiez si elle existe)
            try:
                categorie = Categorie.objects.get(nom_categorie=row["Type"])
            except Categorie.DoesNotExist:
                messages.error(request, f"La catégorie '{row['Type']}' n'existe pas.")
                continue  # Passer à l'itération suivante du DataFrame

            # Obtenir ou créer le produit
            produit, created = Produit.objects.get_or_create(
                nom=row["Produit"],
                defaults={
                    "description": "",
                    "prix": row["Prix"],
                    "id_categorie_id": categorie.id_categorie,
                    "id_fournisseur": None,
                    "stock": 1
                }
            )

            # Obtenir ou créer le client
            # Commencez par vérifier si un client avec l'email existe déjà
            email = row.get("email", "")
            if not email:
                email = f"{row['Name'].replace(' ', '_').lower()}_{index}@vide.com"
            else:
                base_email, domain = email.split("@")
                counter = 0
                # Boucle pour trouver un email unique
                while True:
                    try:
                        client = Client.objects.get(email=email)
                        counter += 1
                        email = f"{base_email}{counter}@{domain}"
                    except Client.DoesNotExist:
                        break

            # Créer ou récupérer le client
            client, created = Client.objects.get_or_create(
                nom=row["Name"],
                defaults={
                    "prenom": "",
                    "adresse": "",
                    "email": email,
                    "telephone": ""
                }
            )

            # Créer la vente
            Vente.objects.create(
                date_vente=row["Date"],
                id_produit=produit,
                quantite=1,  # Ajustez la quantité si nécessaire
                prix_unitaire=row["Prix"],
                id_client=client,
            )

        messages.success(request, "Importation réussie des données des ventes du PDF")
        return redirect('produit')  # Redirigez vers votre vue appropriée

    # Si la méthode n'est pas POST, affichez le formulaire de téléchargement
    return render(request, 'charger/charger.html')

