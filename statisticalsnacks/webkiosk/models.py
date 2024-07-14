from django.db import models # type: ignore

# Create your models here.

class Customer(models.Model): # translates to a customer table
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True) # gets the current date and time when the record is saved and stores that as date joined

    def __str__(self): # django adds id, auto-incrementing
        return f'CUSTOMER #{self.id}, NAME: {self.firstname} {self.lastname}, DATE JOINED: {self.date_joined}'

class Address(models.Model): 
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # foreign key, two arguments: (1) parent model; (2) value of on_delete parameter
    # models.CASCADE = deleting the parent record also deletes its linked records (prevents orphaned records) 

    def __str__(self): 
        return f'CUSTOMER: {self.customer.firstname} {self.customer.lastname}, ADDRESS: {self.street} {self.city}'
    
class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'ITEM #{self.id}, ITEM NAME: {self.name}, DESCRIPTION: {self.description}, PRICE: {self.price}'

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('Cash', 'Cash'), 
        ('Card', 'Card'),
        ('Digital Wallet', 'Digital Wallet')
    ]
    orderdatetime = models.DateTimeField(auto_now_add=True)
    paymentmode = models.CharField(max_length=15, choices=PAYMENT_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def total(self):
        return sum(item.subtotal() for item in self.orderitem_set.all())

    def __str__(self):
        return f'ORDER #{self.id}, CUSTOMER: {self.customer.firstname} {self.customer.lastname}, DATE PLACED: {self.orderdatetime}, MODE OF PAYMENT: {self.paymentmode}'

class OrderItem(models.Model):
    quantity = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def subtotal(self):
        return self.quantity * self.food.price

    def __str__(self):
        return f'ORDER ITEM #{self.id}, NAME: {self.food.name}, PRICE: ₱{self.food.price}, QUANTITY: {self.quantity}'