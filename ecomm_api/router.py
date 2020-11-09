from store_api import views, viewsets
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('products', viewsets.ProductsViewset)
router.register('customer', viewsets.CustomerViewset)
router.register('orderitem', viewsets.OrderItemViewset)