from django.http import HttpResponse # type: ignore
from django.urls import path # type: ignore
from . import views

app_name = 'webkiosk'
urlpatterns = [
    # http://localhost:8000/webkiosk/
    path ('', views.index),

    # http://localhost:8000/webkiosk/customers/
    path('customers/', views.listcustomers, name='customer-list'),

    # http://localhost:8000/webkiosk/customer/new/
    path('customer/new/', views.addcustomer, name='customer-add'),

    # http://localhost:8000/webkiosk/customer/1/
    path('customer/<int:pk>/', views.detailcustomer, name='customer-detail'),

    # http://localhost:8000/webkiosk/customer/1/edit
    path('customer/<int:pk>/edit/', views.updatecustomer, name='customer-update'),

    # http://localhost:8000/webkiosk/customer/1/delete
    path('customer/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),

    # address ----------------------------------

    # http://localhost:8000/webkiosk/customer/1/address/new/
    path('customer/<int:customer_id>/address/new/', views.addaddress, name='address-add'), # parameter has to match the one in the view function

    # food --------------------------------------------

    # http://localhost:8000/webkiosk/food/
    path('food/', views.listfood, name='food-list'),

    # http://localhost:8000/webkiosk/food/new
    path('food/new/', views.addfood, name='food-add'),

    # http://localhost:8000/webkiosk/food/1/
    path('food/<int:food_id>/', views.detailfood, name='food-detail'),

    # http://localhost:8000/webkiosk/food/1/edit
    path('food/<int:food_id>/edit/', views.updatefood, name='food-update'),

    # http://localhost:8000/webkiosk/food/1/delete
    path('food/<int:food_id>/delete/', views.deletefood, name='food-delete'),

    # order ----------------------------------

    # http://localhost:8000/webkiosk/order/new
    path('order/new', views.addorder, name="order-add"),

    # http://localhost:8000/webkiosk/customer/5/order/new
    path('customer/<int:pk>/order/new', views.addcustomerorder, name="customerorder-add"),

    # http://localhost:8000/webkiosk/order/7/edit
    path('order/<int:order_id>/', views.editorder, name='order-edit'),

    # http://localhost:8000/webkiosk/orders
    path('orders/', views.listorders, name="order-list"),

    # http://localhost:8000/webkiosk/order/5/delete
    path('order/<int:order_id>/delete', views.deleteorder, name="order-delete"),

    # http://localhost:8000/webkiosk/order/8/update
    path('order/<int:order_id>/update', views.updateorder, name="order-update"),

    # http://localhost:8000/webkiosk/order/8/info/
    path('order/<int:order_id>/info', views.detailorder, name="order-info"),

    # order items -----------------------------

    # http://localhost:8000/webkiosk/order/1/orderitem/new
    path('order/<int:order_id>/orderitem/new', views.addorderitem, name="orderitem-add"),

    # http://localhost:8000/webkiosk/orderitem/12/edit
    path('orderitem/<int:orderitem_id>/edit', views.updateorderitem, name='orderitem-update'),

    # http://localhost:8000/webkiosk/orderitem/7/delete
    path('orderitem/<int:orderitem_id>/delete/', views.deleteorderitem, name='orderitem-delete'),

]