from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "ShopHome"),
    path('contact/', views.contact, name ="ContactUS"),
    path('about/', views.about, name ="AboutUS"),
    path('tracker/', views.tracker, name ="TrackngStatus"),
    path('search/', views.search, name ="Search"),
    path('productView/', views.productView, name ="Product View"),
    path('checkout/', views.checkout, name ="Checkout"),
    path('careers/', views.careers, name ="Career"),
]