from django.http import JsonResponse
from . import models 


def store(request):
    data = cart_data(request)
    cart_items = data['cartItems']
    products = models.Products.objects.all()
    context = {'products':products, 'cartItems':cart_items}
    return JsonResponse(context)


def cart(request):
    data = cart_data(request)
    return JsonResponse(data)


def cart_data(request):
    customer = request.user.customer
    order = models.Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cart_items = order.get_cart_items
    return {'cartItems':cart_items ,'order':order, 'items':items}