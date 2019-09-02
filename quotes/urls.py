from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('stock_add/', views.stock_add, name="stock_add"),
    path('delete_ticker/<symbol_id>', views.delete_ticker, name="delete"),
]
