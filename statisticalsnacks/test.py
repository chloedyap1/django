from webkiosk.models import Customer, Address

c1 = Customer.objects.get(pk=1)
c2 = Customer.objects.get(pk=2)
c3 = Customer.objects.get(pk=3)

a1 = Address(street='12 Rizal Ave', city='Manila', customer=c1)
a2 = Address(street='24 Rose St', city='Muntinlupa', customer=c1)
a3 = Address(street='34 Bonifacio St', city='Makati', customer=c2)
a4 = Address(street='56 Aguinaldo Ave', city='Mandaluyong', customer=c3)

a1.save()
a2.save()
a3.save()
a4.save()

print(a1.customer)
print(a2.customer)
print(a3.street)
print(a4.city)

print(c1.address_set.all()) # to view all addresses of a particular customer: customer, name of the model, _ , set, .all()
print(c2.address_set.all())
print(c3.address_set.all())