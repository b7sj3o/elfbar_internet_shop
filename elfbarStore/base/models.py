from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name="Нікнейм користувача", unique=True)
    email = models.EmailField(null=True, unique=True, verbose_name='Ваш E-mail')
    phone = models.CharField(null=True, unique=True, max_length=9, verbose_name="Номер телефону")    

    REQUIRED_FIELDS = []

class Types(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    
class Flavours(models.Model):
    flavour = models.CharField(max_length=100)
    is_avialable = models.BooleanField(default=True)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.flavour

class Product(models.Model):
    type = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name="Модель")
    name = models.CharField(max_length=255, verbose_name="Назва")
    slug_name = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Назва (замість пробілів '_')")
    description1 = models.TextField(verbose_name="Характеристики товару")
    description2 = models.TextField(verbose_name="Опис товару")
    flavours = models.ManyToManyField(Flavours, blank=True, verbose_name="Наявні смаки")
    image = models.ImageField(blank=True, upload_to='base/img/products', verbose_name="Фото")
    price = models.PositiveIntegerField(verbose_name="Ціна")

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    chosen_flavour = models.CharField(max_length=100, default='no flavour')
    quantity = models.PositiveIntegerField(default=1)




