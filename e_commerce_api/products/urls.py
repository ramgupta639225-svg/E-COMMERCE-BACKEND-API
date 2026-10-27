from django.urls import path, include
from .views import ProductDetailsView, ProductListView

urlpatterns = [

    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailsView.as_view(), name="product_detail")



]

