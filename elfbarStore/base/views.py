from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateProduct, CreateFlavour, CreateType, RegistrationForm
from .models import Product, Types, User, Cart, CartItem


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

    forms = RegistrationForm()

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Ви успішно увійшли в акаунт')
            return redirect('home')
        else:
            messages.success(request, 'Трапилася помилка. Спробуйте знову')
            return redirect('login')

    context = {
        'forms': forms
    }

    return render(request, 'base/login.html', context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            messages.success(request, 'Ви успішно зареєструвались')
            return redirect('home')

        messages.success(request, 'Трапилася помилка')

    return render(request, 'base/login.html')


def addToCart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    chosen_flavour = str(request.POST.get('chosen_flavour'))
    quantity = int(request.POST.get('quantity'))

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            chosen_flavour=chosen_flavour,
            quantity=quantity
        )

        if not created:
            cart_item.save()

    else:
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


def createBaseProduct(request, pk, page):
    forms = pk()
    if request.POST:
        form = pk(request.POST, request.FILES)
        if form.is_valid():
            _form = form.save(commit=False)
            if page == 'create-flavour':
                _form.flavour = _form.flavour.capitalize()
                _form.save()
            elif page == 'create-type':
                _form.type = _form.type.upper()

            _form.save()
            return redirect('home')

        messages.success(request, 'Трапилася помилка')
        return redirect(page)

    context = {
        'forms': forms
    }
    return render(request, f"base/{page}.html", context)


def createProduct(request):
    return createBaseProduct(request, CreateProduct, 'create-product')


def createFlavour(request):
    return createBaseProduct(request, CreateFlavour, 'create-flavour')


def createType(request):
    return createBaseProduct(request, CreateType, 'create-type')

# ----------------- READ -----------------

def userCart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        cart_items = request.session.get('cart', {}).values()

    context = {
        'cart': cart_items
    }
    return render(request, 'base/cart.html', context)


# ----------------- UPDATE -----------------

# ----------------- DELETE -----------------

def removeCartItem(request, pk, chosen_flavour):
    if request.user.is_authenticated:
        product = Product.objects.get(id=pk)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
    else:
        cart = request.session.get('cart', {})
        key = f"{pk}_{chosen_flavour}"
        del cart[key]

        request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER'))


def deleteProduct(request, pk):
    referer = request.META.get('HTTP_REFERER', None)

    product = Product.objects.get(id=pk)
    product.delete()

    return redirect(referer)


def logoutUser(request):
    logout(request)
    messages.success(request, 'Ви вийшли з акаунту')
    return redirect('home')
