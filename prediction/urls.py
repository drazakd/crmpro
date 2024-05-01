from django.urls import path
from . import views

urlpatterns = [
    path('predict-sales/', views.predict_sales, name='predict_sales')
]
