from django.contrib import admin
from .models import Customer, Address, Food, OrderItem, Order

admin.site.register([Customer, Address, Food, OrderItem, Order])