from rest_framework import viewsets, permissions
from . import models
from . import serializers

# list(), retrive() -> GET
# create -> POST
# update -> PUT
# destroy() -> DELETE

# ViewSets define the view behavior.
class ProductsViewset(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer


class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class OrderItemViewset(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer