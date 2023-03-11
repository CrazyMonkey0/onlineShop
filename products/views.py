from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Category, Products, Subcategory


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
