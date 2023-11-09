from django.urls import path
from . import views

urlpatterns = [
    path('', views.created_products_view, name='index'),
    path('parse/', views.imported_products_view, name='imported_products_view')
]
