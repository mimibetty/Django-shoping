from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def category(request):
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    if active_category:
        products  = Product.objects.filter(category__slug=active_category)
    
    context = {'categories': categories, 'active_category': active_category, 'products': products}
    return render(request, 'app/category.html', context)
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        keys = Product.objects.filter(name__icontains = searched)

    if (request.user.is_authenticated):
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else :
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    products = Product.objects.all()
    return render(request, 'app/search.html',{'products': products, 'cartItems': cartItems, 
    'keys': keys , 'searched': searched, 'user_not_login': user_not_login, 'user_login': user_login})

def register(request):
    form = CreateUserForm()
    context = {'form' : form, 'user_not_login': 'show', 'user_login': 'hidden'}

    if (request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form' : form, 'message': 'User created successfully', 'user_not_login': 'show', 'user_login': 'hidden'}
            return redirect('login')
        else:
            context = {'form' : form, 'message': 'User creation failed', 'user_not_login': 'show', 'user_login': 'hidden'}
 
    return render(request, 'app/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)  
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    user_not_login = "show"
    user_login = "hidden"
        
    context = { 'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def home(request):
    if (request.user.is_authenticated):
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
     
        # show status login
        user_not_login = "hidden"
        user_login = "show"
        print(f"{order} orderrrr")
        print(f"{created} createeee")


    else :
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"

    # print('ITEMS:', items)
    categories = Category.objects.filter(is_sub=False)
    products = Product.objects.all()
    # print(products)  # Thêm dòng này để kiểm tra xem products có dữ liệu hay không
    context = {'products': products, 'cartItems': cartItems, 'user_not_login': user_not_login, 
               'user_login': user_login, 'categories': categories}
    print(context)
    return render(request, 'app/home.html', context)


def cart(request):
    if (request.user.is_authenticated):
        customer = request.user
        # print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else :
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"

    context = {'items': items, 'order': order, 'cartItems': cartItems, 
               'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'app/cart.html', context)


def detail(request):
    if (request.user.is_authenticated):
        customer = request.user
        # print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else :
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    id = request.GET.get('id', '')
    products = Product.objects.filter(id = id)
    context = {'items': items, 'order': order, 'cartItems': cartItems, 
               'user_not_login': user_not_login, 'user_login': user_login, 'products': products}
    return render(request, 'app/detail.html', context)

def checkout(request):
    if (request.user.is_authenticated):
        customer = request.user
        # print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else :
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"

    context = {'items': items, 'order': order, 'cartItems': cartItems, 
               'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'app/checkout.html', context)

def updateItem(request):
    data =  json.loads(request.body)
    productId = data['productId']
    action = data['action']             
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("added" , safe= False)


def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    print("updae_product_view")
    print(product)
    print(categories)
    
    return render(request, 'app/update_product.html', {'product': product, 'categories': categories})

@csrf_exempt
def update_product(request, pk):
    print("request.method", pk)

    if request.method == 'PUT':
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.digital = data.get('digital', product.digital)
        product.detail = data.get('detail', product.detail)

        if 'category' in data:
            product.category.set(data['category'])

        product.save()

        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'digital': product.digital,
            'detail': product.detail,
            'category': [cat.id for cat in product.category.all()]
        })

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


def add_product_page(request):
    return render(request, 'app/create_product.html')

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        categories_data = data.pop('category', [])
        product = Product.objects.create(**data)
        for category_id in categories_data:
            category = Category.objects.get(id=category_id)
            product.category.add(category)
        return JsonResponse({'message': 'Product created successfully!', 'product_id': product.id})