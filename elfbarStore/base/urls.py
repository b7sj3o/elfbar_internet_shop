from django.urls import path
from . import views

urlpatterns = [
    # --- HOME ---
    path('', views.home, name='home'),

    # --- CREATE ---
    path('add-to-cart<str:product_id>', views.addToCart, name='add-to-cart'),
    path('create-product', views.createProduct, name='create-product'),
    path('create-flavour', views.createFlavour, name='create-flavour'),
    path('create-type', views.createType, name='create-type'),


    # --- DELETE ---
    path('remove-from-cart/<str:pk>/<str:chosen_flavour>', views.removeCartItem, name='remove-from-cart'),
    path('delete-product<int:pk>', views.deleteProduct, name='delete-product'),
    
    
    # --- UPDATE ---
    
    
    # --- READ -----
    path('cart', views.userCart, name='cart'),

    # --- AUTH -----

    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),



]