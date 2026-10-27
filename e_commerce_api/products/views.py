from django.shortcuts import render

# Create your views here.
from .serializers import ProductSerializer
from rest_framework import generics
from .models import Product

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
