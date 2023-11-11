from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.created_products_view, name='index'),
    path('parse/', views.imported_products_view, name='imported_products_view'),
    path('product/<int:id>/', views.product_view_detailed, name='detailed_product'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', views.login_view.as_view()),
    # path('logout/', views.logout_view, name='logout'),
]
