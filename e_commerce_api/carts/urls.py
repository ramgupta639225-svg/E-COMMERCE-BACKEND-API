from django.urls import path, include
from .views import AddToCartView, CartDetailsView


urlpatterns = [

    path('', CartDetailsView.as_view(), name="cart_detail"),
    path('add/', AddToCartView.as_view(), name="add_to_cart"),


]