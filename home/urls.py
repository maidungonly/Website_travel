from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('review/', views.review),
    path('postdanang/',views.reviewpost),
    path('support/',views.support),
    path('register/',views.register_page),
    path('signin/', views.login_page, name='login_page'),
    path('tourticket/',views.tourticket),
    path('moveticket/',views.moveticket),
    path('roomticket/',views.roomticket),
    path('otherservicesticket/',views.otherservicesticket),
    path('order/<slug:slug>',views.order),
    path('moveticket/',views.moveticket),
    path('roomticket/',views.roomticket),
    path('areareview/',views.areareview),
    path('book_tour/<slug:slug>/',views.book_tour, name='product_detail'),
    path('contact/',views.contact), 
    path('cart/',views.cart) 
    # path('logout/', auth_views.logout, {'home':'/'}, name='logout')
]

