from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=50,default="Regular Brand")
    product_type = models.CharField(max_length=50)
    name = f"{brand} {product_type}"
    base_price = models.IntegerField()

    @property
    def full_name(self):
        return f"{self.brand} {self.product_type}"

class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class SalesOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)
    product = models.ManyToManyField(Product, through="OrderItem")
    status = models.TextChoices("In process", "Completed", "Canceled",)
    
class OrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_discount = models.DecimalField()
    quantity = models.PositiveIntegerField(default=0)

    @property
    def product_price(self):
        return self.product.base_price