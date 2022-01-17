from django.contrib.auth.models import User
from django.db import reset_queries
from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *

from django.utils import timezone
# Create your views here.


def home(request):
    products = Product.objects.all()
    areas = Area.objects.all()
    # product = products[0].image
    # print('Debug')
    return render(request, 'pages/home.html', {'products' : products, 'areas': areas})


def review(request):
    areas = Area.objects.all()
    context = {'areas': areas}
    return render(request, 'pages/review.html',context)


def reviewpost(request):
    return render(request, 'pages/reviewpost.html')

def support(request):
    return render(request, 'pages/support.html')


def tourticket(request):
    products = Product.objects.all()
    return render(request, 'pages/tourticket.html',{'products' : products})

def moveticket(request):
    moves = Move.objects.all()
    return render(request, 'pages/moveticket.html',{'moves' : moves})

def roomticket(request):
    rooms = Room.objects.all()
    return render(request, 'pages/roomticket.html',{'rooms' : rooms})

def otherservicesticket(request):
    return render(request, 'pages/otherservicesticket.html')

import datetime


from django.core import serializers

def order(request, slug):
    try:
        product = Product.objects.get(slug = slug)
    except:
        product = Room.objects.get(slug=slug)
    vouchers = Voucher.objects.all()
    serialized_vouchers = serializers.serialize("json", Voucher.objects.all())
    if request.method == 'POST':
        customer = \
            request.user.customer if \
                request.user.is_authenticated and hasattr(request.user, 'customer') else Customer.objects.create(
                    user=None, 
                    email=request.POST['email'], 
                    name=request.POST['name'], 
                    phone_number=request.POST['phone']
                )
        voucher = request.POST['voucher']
        order_item = OrderItem.objects.create(
            product=product if isinstance(product, Product) else None,
            room=product if isinstance(product, Room) else None,
            quantity=request.POST['quantity'],
            voucher=Voucher.objects.get(code=voucher) if voucher else None
        )
        Order.objects.create(
            customer=customer,
            date_order=timezone.now(),
            order_item=order_item,
            complete=True,
            transaction_id=int(datetime.datetime.now().timestamp()),
            payment_option=request.POST['pay']
        )
        messages.success(request, 'Order completed!')
        # return redirect('home')

    return render(request, 'pages/order.html', context={
        'product': product, 
        'vouchers': vouchers, 
        'serialized_vouchers': serialized_vouchers
    })


def areareview(request):
    return render(request, 'pages/areareview.html')

def book_tour(request, slug):
    context = {}
    try:
        product =  Product.objects.get(slug=slug)
    except:
        product = Room.objects.get(slug=slug)
    info_dd = product.info_dd
    product.info_dd = [d for d in info_dd.split('.') if d]
    context['product'] = product
    return render(request, 'pages/dattour.html', context=context)

def contact(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        name = request.POST['name']
        phone_number = request.POST['phone']
        email = request.POST['mail']
        password = request.POST['password1']
        profile_picture = request.FILES['profile']

        customer.name = name if name else customer.name
        customer.phone_number = phone_number
        customer.email = email
        customer.profile_picture = profile_picture

        customer.save()

        #request.user.customer = customer
        user = request.user
        user.set_password(password)
        user.save()

        user = authenticate(request, username=user.username, password=password)

        messages.success(request, 'Info changed successfully!')

    return render(request, 'pages/contact.html')

def cart(request):
    return render(request, 'pages/cart.html')

def register_page(request):
    form = None
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Customer.objects.create(
                user=user,
                name=username,
                email=form.cleaned_data.get('email')
            )

            messages.success(request, 'Account was created')
            return redirect('login_page')
    context = {'form' : form}
    
    return render(request, 'pages/register.html', context)

def login_page(request):
    if request.method == 'POST':
        if 'logout' not in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else: 
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'pages/signin.html')
        else:
            logout(request)
        
    return render(request, 'pages/signin.html')

# def logout_user(request):
#     logout(request)
#     return redirect('login')