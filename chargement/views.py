
from django.shortcuts import render, redirect
from django.contrib import messages
import csv

from produit.models import Produit
from vente.models import Client, Vente
from fournisseur.models import Categorie
import tabula
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from vente.models import Vente


# Vue pour importer les ventes à partir d'un fichier PDF
def import_ventes_pdf(request):
    if request.method == 'POST':
        # Vérifier si un fichier a été soumis
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

        # Nettoyer les données : remplacer les valeurs NaN et les chaînes vides
        df_concat.replace({np.nan: "", "": "0.0"}, inplace=True)

        # Convertir les colonnes de prix en float
        df_concat['Prix'] = df_concat['Prix'].str.replace(',', '.').str.strip()
        df_concat['Prix'] = pd.to_numeric(df_concat['Prix'], errors='coerce')

        # Remplacer les valeurs nan dans Prix par une valeur par défaut
        df_concat['Prix'].fillna(0.0, inplace=True)

        # Insérer les données dans les tables de base de données
        for index, row in df_concat.iterrows():
            # Vérifier si la catégorie existe, sinon la créer
            categorie, created = Categorie.objects.get_or_create(nom_categorie=row["Type"])

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
            email = f"{row['Name'].replace(' ', '_').lower()}_{index}@vide.com"
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
            try:
                Vente.objects.create(
                    date_vente=row["Date"],
                    id_produit=produit,
                    quantite=1,  # Ajustez la quantité si nécessaire
                    prix_unitaire=row["Prix"],
                    id_client=client,
                )
            except Exception as e:
                messages.error(request, f"Erreur lors de la création de la vente : {str(e)}")
                continue

        messages.success(request, "Importation réussie des données des ventes du PDF")
        return redirect('produit')

    # Si la méthode n'est pas POST, affichez le formulaire de téléchargement
    return render(request, 'charger/charger.html')



def exporter_csv(request):
    # Créez une réponse HTTP avec le type de contenu CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ventes.csv"'

    # Créez un writer CSV
    writer = csv.writer(response)

    # Écrivez l'en-tête CSV (les noms de colonnes)
    writer.writerow(['ID', 'Date de vente', 'Produit', 'Prix unitaire', 'Quantité', 'Client'])

    # Récupérez toutes les ventes de la table
    ventes = Vente.objects.all()

    # Écrivez chaque vente dans le CSV
    for vente in ventes:
        try:
            # Assurez-vous que l'accès aux relations ne déclenche pas d'exception
            produit_nom = vente.id_produit.nom if vente.id_produit else 'Produit manquant'
            client_nom = vente.id_client.nom if vente.id_client else 'Client manquant'

            writer.writerow([
                vente.id_vente,
                vente.date_vente,
                produit_nom,
                vente.prix_unitaire,
                vente.quantite,
                client_nom
            ])
        except AttributeError as e:
            # Gérez l'exception ici (afficher un message, passer à la vente suivante, etc.)
            continue

    return response


