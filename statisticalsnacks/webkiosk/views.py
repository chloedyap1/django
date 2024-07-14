from django.contrib import messages # type: ignore
from django.http import HttpResponse # type: ignore
from django.shortcuts import get_object_or_404, redirect, render # type: ignore

from .models import Customer, Address, Food, Order, OrderItem

from .forms import CustomerForm, AddressForm, FoodForm, OrderForm, OrderitemForm, CustomerorderForm

# Create your views here.

def index(request):
    return render(request, 'webkiosk/base_template.html')

def listcustomers(request):
    customerlist = Customer.objects.all()
    context = { 'customerlist': customerlist }
    return render(request, 'webkiosk/customer_list.html', context)

def addcustomer(request):
    if request.method == 'GET': # if we simply visit the url, it is a 'GET' request - just creates an empty form
        cf = CustomerForm()
    elif request.method == 'POST': # click the button - 'POST' request inserts new customer record
        cf = CustomerForm(request.POST) # creates a new customer form with all the data submitted
        if cf.is_valid():
            cf.save()
            return redirect('webkiosk:customer-list') # using names, can edit the url pattern without needing to change the name

    context = { 'form': cf, 'actionname': 'Add'}
    return render(request, 'webkiosk/customer_form.html', context)

def detailcustomer(request, pk):
    c = Customer.objects.get(id=pk) # use get with fields that are unique so only one record will match
    context = { 'customer': c }
    return render(request, 'webkiosk/customer_detail.html', context)

def updatecustomer (request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = CustomerForm(instance=customer) # instance would be the customer object whose record we wanna edit; we will see the first and last name of the customer
    elif request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record updated successfully.')
    context = {'form':form, 'actionname': 'Edit'}
    return render (request, 'webkiosk/customer_form.html', context)

def deletecustomer(request, pk):
    c = get_object_or_404(Customer, id=pk)
    if request.method == 'GET':
        context = { 'customer': c }
        return render(request, 'webkiosk/customer_delete.html', context)
    elif request.method == 'POST':
        c.delete()
        return redirect('webkiosk:customer-list')
    
# address ----------------------------

def addaddress(request, customer_id):
    if request.method == 'GET':
        customer = get_object_or_404(Customer, id=customer_id)
        form = AddressForm(initial={'customer':customer})
    elif request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:customer-detail', pk=customer_id)

    context = {'form' : form}
    return render(request, 'webkiosk/address_form.html', context)

# food ----------------------------------

def listfood(request):
    foodlist = Food.objects.all()
    context = { 'foodlist': foodlist }
    return render(request, 'webkiosk/food_list.html', context)

def addfood(request):
    if request.method == 'GET': 
        ff = FoodForm()
    elif request.method == 'POST':
        ff = FoodForm(request.POST)
        if ff.is_valid():
            ff.save()
            return redirect('webkiosk:food-list')
    context = { 'form': ff, 'actionname': 'Add'}
    return render(request, 'webkiosk/food_form.html', context)

def detailfood(request, food_id):
    f = Food.objects.get(id=food_id) 
    context = { 'food': f}
    return render(request, 'webkiosk/food_detail.html', context)

def updatefood (request, food_id):
    food = Food.objects.get(id=food_id)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item details updated successfully.')
    context = {'form':form, 'actionname': 'Edit'}
    return render (request, 'webkiosk/food_form.html', context)

def deletefood(request, food_id):
    f = get_object_or_404(Food, id=food_id)
    if request.method == 'GET':
        context = { 'food': f }
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == 'POST':
        f.delete()
        return redirect('webkiosk:food-list')

# order --------------------------

def addcustomerorder(request, pk): # automatically selects the customer for the order - redirected from the customer details page
    if request.method == 'GET': 
        customer = get_object_or_404(Customer, id=pk)
        cof = CustomerorderForm(initial={'customer':customer})
    elif request.method == 'POST':
        cof = CustomerorderForm(request.POST)
        if cof.is_valid():
            order = cof.save()
            return redirect('webkiosk:orderitem-add', order_id=order.id)
    context = { 'form': cof, 'actionname': 'Add'}
    return render(request, 'webkiosk/order_form.html', context)

def addorder(request):
    if request.method == 'GET': 
        of = OrderForm()
    elif request.method == 'POST':
        of = OrderForm(request.POST)
        if of.is_valid():
            order = of.save()
            return redirect('webkiosk:orderitem-add', order_id=order.id)
    context = { 'form': of, 'actionname': 'Add'}
    return render(request, 'webkiosk/order_form.html', context)

def listorders(request):
    orderlist = Order.objects.all()
    context = {'orderlist': orderlist}
    return render(request, 'webkiosk/order_list.html', context)

def deleteorder(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'GET':
        context = {'order': order}
        return render(request, 'webkiosk/order_delete.html', context)
    if request.method == 'POST':
        order.delete()
        return redirect ('webkiosk:order-list')
    
def updateorder(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'GET':
        form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:order-edit', order_id=order_id)
    context = {'form':form, 'actionname':'Edit'}
    return render(request, 'webkiosk/order_update_form.html', context)

def editorder (request, order_id):
    o = Order.objects.get(id=order_id)
    oi = OrderItem.objects.filter(order = order_id)
    context = {'order':o, 'orderitem':oi}
    return render(request, 'webkiosk/order_edit.html', context)

def detailorder (request, order_id):
    o = Order.objects.get(id=order_id)
    oi = OrderItem.objects.filter(order = order_id)
    context = {'order':o, 'orderitem':oi}
    return render(request, 'webkiosk/order_detail.html', context)

# order items --------------------

def addorderitem(request, order_id):
    if request.method == 'GET':
        order = get_object_or_404(Order, id=order_id)
        form = OrderitemForm(initial={'order':order})
    elif request.method == 'POST':
        form = OrderitemForm(request.POST)
        if form.is_valid():
            form.save()
            if 'add_item' in request.POST:
                return redirect('webkiosk:orderitem-add', order_id=order_id)
            elif 'submit' in request.POST:
                return redirect('webkiosk:order-edit', order_id=order_id)
    context = {'form' : form, 'actionname':'Add'}
    return render(request, 'webkiosk/orderitem_form.html', context)

def updateorderitem (request, orderitem_id):
    orderitem = get_object_or_404(OrderItem, id=orderitem_id)
    order_id = orderitem.order.id
    if request.method == 'GET':
        form = OrderitemForm(instance=orderitem)
    elif request.method == 'POST':
        form = OrderitemForm(request.POST, instance=orderitem)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:order-edit', order_id=order_id)
    context = {'form':form, 'actionname': 'Edit'}
    return render (request, 'webkiosk/order_update_form.html', context)

def deleteorderitem(request, orderitem_id):
    orderitem = get_object_or_404(OrderItem, id=orderitem_id)
    order_id = orderitem.order.id
    if request.method == 'GET':
        context = { 'orderitem': orderitem }
        return render(request, 'webkiosk/orderitem_delete.html', context)
    elif request.method == 'POST':
        orderitem.delete()
        return redirect('webkiosk:order-edit', order_id=order_id)