from django.forms import ModelForm, HiddenInput # type: ignore
from .models import Customer, Address, Food, Order, OrderItem

class CustomerForm(ModelForm):
    class Meta:
        model = Customer 
        fields = ['firstname', 'lastname']# which model & (input) fields we want to work with

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'customer']
        widgets = { 'customer': HiddenInput} # to hide customer

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'paymentmode']

class OrderitemForm(ModelForm):
    class Meta: 
        model = OrderItem
        fields = ['food', 'quantity', 'order']
        widgets = { 'order': HiddenInput}

class CustomerorderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer','paymentmode']
        widgets = { 'customer': HiddenInput}