from django.urls import path, include
from .views import AddToCartView, CartDetailsView, UpdateCartItemView


urlpatterns = [

    path('', CartDetailsView.as_view(), name="cart_detail"),
    path('add/', AddToCartView.as_view(), name="add_to_cart"),
    path('items/<int:item_id>/', UpdateCartItemView.as_view(), name="updated_cart_item"),


]