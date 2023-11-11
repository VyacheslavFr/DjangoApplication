from django.urls import path
from . import views

urlpatterns = [
    path('', views.created_products_view, name='index'),
    path('parse/', views.imported_products_view, name='imported_products_view'),
    path('product/<int:id>/', views.product_view_detailed, name='detailed_product'),
    path('profile', views.profile_view, name='profile'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login_view.as_view()),
    # path('logout/', views.logout_view, name='logout'),
]
