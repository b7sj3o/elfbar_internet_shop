from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Types, User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateProduct

def home(request):
    # request.session['cart'] = {}
    types = Types.objects.all().order_by('-id')
    products = Product.objects.all().order_by('name')

    context = {
        'types': types,
        'products': products
    }
    return render(request, 'base/index.html', context)


# ----------------- CREATE -----------------

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Трапилася помилка. Спробуйте знову')
            return redirect('login')

    return render(request, 'base/login.html')

def registerUser(request):
    if request.POST:
        pass
    return render(request, 'base/login.html')

def addToCart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    chosen_flavour = str(request.POST.get('chosen_flavour'))
    quantity = int(request.POST.get('quantity'))
    key = f"{product_id}_{chosen_flavour}"
    cart = request.session.get('cart', {})

    if key in cart:
        cart[key]['quantity'] += quantity
    else:
        cart[key] = {
            'name': product.name,
            'chosen_flavour': chosen_flavour,
            'image': str(product.image),
            'price': product.price,
            'quantity': quantity,
            'id': product_id
        }

    request.session['cart'] = cart

    return redirect('cart')

def createProduct(request):
    forms = CreateProduct()
    if request.POST:
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        messages.success(request, 'Трапилася помилка')
        return redirect('create-product')

    context = {
        'forms': forms
    }
    return render(request, 'base/create-product.html', context)
# ----------------- READ -----------------
def cart(request):
    cart = request.session.get('cart', {}).values()
    return render(request, 'base/cart.html', {'cart': cart})


# ----------------- UPDATE -----------------

# ----------------- DELETE -----------------

def removeCartItem(request, pk, chosen_flavour):
    cart = request.session.get('cart', {})
    key = f"{pk}_{chosen_flavour}"
    del cart[key]

    request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER'))

def logoutUser(request):
    logout(request)
    messages.success(request, 'Ви вийшли з акаунту')
    return redirect('home')