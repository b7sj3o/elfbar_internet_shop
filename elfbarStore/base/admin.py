from django.contrib import admin
from .models import Product, Flavours, Types

admin.site.register(Product)
admin.site.register(Flavours)
admin.site.register(Types)
