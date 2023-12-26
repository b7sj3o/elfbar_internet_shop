from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add-to-cart<str:product_id>', views.addToCart, name='add-to-cart'),
    path('remove-from-cart/<str:pk>/<str:chosen_flavour>', views.removeCartItem, name='remove-from-cart'),
    path('cart', views.cart, name='cart'),

    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),

    path('create-product', views.createProduct, name='create-product')

]