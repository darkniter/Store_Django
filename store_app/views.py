from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from store_app.models import Product
from store_app.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
