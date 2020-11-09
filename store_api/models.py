from django.db import models
from django.contrib.auth.models import User

## Store Products
class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    colour = models.CharField(max_length=50, null=True)
    euler_char = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

## Customer
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

## Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

## Customers Order
class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    # price of basket
    @property 
    def get_total(self):
        total = self.product.price * self.quantity
        return total