from django.urls import path, re_path
from . import views

urlpatterns = [
    # --- HOME ---
    path('', views.home, name='home'),


    # --- CREATE ---
    path('create/<str:pk>/', views.addToCartAJAX, name='create'),
    path('create-product', views.createProduct, name='create-product'),
    path('create-flavour', views.createFlavour, name='create-flavour'),
    path('create-type', views.createType, name='create-type'),

    # --- READ -----
    path('cart', views.userCart, name='cart'),
    path('product/<slug:slug_name>', views.productDetail, name='product_detail'),

    # --- UPDATE ---
    path('edit-product<int:pk>', views.editProduct, name='edit-product'),

    # --- DELETE ---
    path('remove-from-cart/<str:pk>/<str:chosen_flavour>',views.removeCartItem, name='remove-from-cart'),
    path('delete-product<int:pk>', views.deleteProduct, name='delete-product'),

    # --- AUTH -----

    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),


    # --- OTHERS ---
    re_path(r'^(?P<pk>[\s\S]*)/$', views.page_404, name='page_404'),


]
