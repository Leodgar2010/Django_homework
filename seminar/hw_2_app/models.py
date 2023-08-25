from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField
    address = models.TextField()
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
       return f'{self.name}, phone: {self.surname}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
       return f'{self.name}, price: {self.price}'

class Order (models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f'{self.customer} заказал {self.products}'