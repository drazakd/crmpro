from django.shortcuts import render
from django.http import HttpResponse
from vente.models import Vente  # Modèle de vente
import pandas as pd
from prophet import Prophet


# Create your views here.

def predict_sales(request):
    # Récupérer les données de vente depuis la base de données Django
    ventes = Vente.objects.select_related('id_produit').values('date_vente', 'quantite', 'id_produit__nom')

    # Convertir les données en DataFrame pandas
    df = pd.DataFrame(ventes)

    # Convertir la colonne de date en datetime
    df['date'] = pd.to_datetime(df['date_vente'])

    # Renommer les colonnes pour correspondre à ce que Prophet attend
    df = df.rename(columns={'date_vente': 'ds', 'quantite': 'y', 'id_produit__nom': 'product'})

    # Supprimer les informations de fuseau horaire de la colonne 'ds'
    df['ds'] = df['ds'].dt.tz_localize(None)

    # Créer une liste des produits uniques
    products = df['product'].unique()

    # Dictionnaire pour stocker les prédictions de chaque produit
    predictions = {}

    # Pour chaque produit, entraîner un modèle et prédire les ventes en avril 2024
    for product in products:
        # Filtrer les données pour le produit actuel
        product_df = df[df['product'] == product]

        # Créer un modèle Prophet
        model = Prophet()

        # Entraîner le modèle sur les données historiques du produit
        model.fit(product_df[['ds', 'y']])

        # Créer un DataFrame pour les dates de prédiction (avril 2024)
        future_dates = pd.DataFrame({'ds': pd.date_range(start='2024-04-01', end='2024-04-30')})

        # Faire la prédiction
        forecast = model.predict(future_dates)

        # Calculer le total des quantités prévues pour le produit en avril 2024
        total_predicted_sales = forecast['yhat'].sum()

        # Stocker la prédiction dans le dictionnaire
        predictions[product] = total_predicted_sales

    # Trouver le produit avec les ventes prévues les plus élevées
    best_selling_product = max(predictions, key=predictions.get)

    # Afficher les résultats
    context = {
        'best_selling_product': best_selling_product,
        'predicted_sales': predictions[best_selling_product]
    }

    return render(request, 'profils/dashboard.html', context)




# def predict_sales(request):
#     # Récupérer les données de vente depuis la base de données Django
#     ventes = Vente.objects.select_related('id_produit').values('date_vente', 'quantite', 'id_produit__nom')
#
#     # Convertir les données en DataFrame pandas
#     df = pd.DataFrame(ventes)
#
#     # Convertir les colonnes de date en datetime
#     df['date'] = pd.to_datetime(df['date_vente'])
#
#     # Renommer les colonnes pour correspondre à ce que Prophet attend
#     df = df.rename(columns={'date_vente': 'ds', 'quantite': 'y', 'id_produit__nom': 'product'})
#
#     # Supprimer les informations de fuseau horaire de la colonne 'ds'
#     df['ds'] = df['ds'].dt.tz_localize(None)
#
#     # Créer une liste des produits uniques
#     products = df['product'].unique()
#
#     # Récupérer le mois et l'année sélectionnés par l'utilisateur dans la requête
#     selected_month = int(request.GET.get('mois', 4))  # Valeur par défaut : avril
#     selected_year = int(request.GET.get('annee', 2024))  # Valeur par défaut : 2024
#
#     # Définir la plage de dates pour la prédiction
#     start_date = f"{selected_year}-{selected_month:02d}-01"
#     end_date = f"{selected_year}-{selected_month:02d}-30"
#
#     # Créer une plage de dates à prédire
#     future_dates = pd.date_range(start=start_date, end=end_date)
#
#     # Dictionnaire pour stocker les prédictions de chaque produit
#     predictions = {}
#
#     # Pour chaque produit, entraîner un modèle et prédire les ventes pour le mois et l'année sélectionnés
#     for product in products:
#         # Filtrer les données pour le produit actuel
#         product_df = df[df['product'] == product]
#
#         # Créer un modèle Prophet
#         model = Prophet()
#
#         # Entraîner le modèle sur les données historiques du produit
#         model.fit(product_df[['ds', 'y']])
#
#         # Prédire les ventes
#         forecast = model.predict(pd.DataFrame({'ds': future_dates}))
#
#         # Calculer le total des ventes prévues pour le produit pour la période sélectionnée
#         total_predicted_sales = forecast['yhat'].sum()
#
#         # Stocker la prédiction dans le dictionnaire
#         predictions[product] = total_predicted_sales
#
#     # Trouver le produit avec les ventes prévues les plus élevées
#     best_selling_product = max(predictions, key=predictions.get)
#
#     # Préparer les listes de mois et d'années pour le contexte
#     months = list(range(1, 13))
#     years = list(range(2024, 2031))
#
#     # Préparer le contexte pour rendre le template
#     context = {
#         'best_selling_product': best_selling_product,
#         'predicted_sales': predictions[best_selling_product],
#         'selected_month': selected_month,
#         'selected_year': selected_year,
#         'months': months,
#         'years': years,
#     }
#
#     # Rendre le template avec le contexte
#     return render(request, 'profils/dashboard.html', context)