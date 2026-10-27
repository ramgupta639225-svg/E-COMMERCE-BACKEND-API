from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product
# Create your views here.


class CartDetailsView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request):
        product_id = request.data.get("product")
        quantity = request.data.get("quantity", 1)

        try:
            quantity = int(quantity)

        except (TypeError, ValueError):
            return Response ({"error": "Quantity must be a valid integer"}, status=status.HTTP_400_BAD_REQUEST)


        if quantity < 1:
            return Response ({"error": "Quantity muse be at least 1."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id, is_active=True)

        except (Product.DoesNotExist, ValueError, TypeError):
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)


        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={"quantity": quantity})

        if not item_created:
            cart_item.quantity += quantity
            cart_item.save(update_fields=["quantity"])


        serializer = CartItemSerializer(cart_item)

        return Response (serializer.data, status=status.HTTP_201_CREATED)



