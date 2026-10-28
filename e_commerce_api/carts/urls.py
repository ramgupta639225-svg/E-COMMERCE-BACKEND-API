from django.urls import path, include
from .views import AddToCartView, CartDetailsView, UpdateCartItemView, DeleteCartItemView


urlpatterns = [

    path('', CartDetailsView.as_view(), name="cart_detail"),
    path('add/', AddToCartView.as_view(), name="add_to_cart"),
    path('items/<int:item_id>/', UpdateCartItemView.as_view(), name="updated_cart_item"),
    path('items/<int:item_id>/remove', DeleteCartItemView.as_view(), name="delete_cart_item"),


]