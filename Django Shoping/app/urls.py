from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"), 
    path('update_item/', views.updateItem, name="update_item"), 
    path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutPage, name="logout"), 
    path('register/', views.register, name="register"), 
    path('category/', views.category, name="category"), 
    path('search/', views.search, name="search"), 
    path('detail/', views.detail, name="detail"), 

# update Product
    path('products/update/<int:pk>/', views.update_product_view, name='update_product_view'),
    path('api/v1/products/<int:pk>/', views.update_product, name='update_product'),

# add Product
    path('api/v1/products/', views.create_product, name='product_create'),
    path('products/create', views.add_product_page, name='add_product_page'),

]
