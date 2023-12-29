from django.contrib import admin
from .models import Product, Flavours, Types, Cart, CartItem

admin.site.register(Product)
admin.site.register(Flavours)
admin.site.register(Types)
admin.site.register(Cart)
admin.site.register(CartItem)
