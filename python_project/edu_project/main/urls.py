from django.urls import path
from . import views
from rest_framework import routers


urlpatterns = [
    path('all_products/', views.AllProductsView.as_view()), # Получение всех продуктов пользователя по логину. 
    path('product/', views.CurrentProductView.as_view()), # Получение данных по конкретному продукту. 
    path('statistic/', views.StatisticsView.as_view()), # Статистика по продуктам. 
]