from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=50,default="Regular Brand", null=False)
    product_type = models.CharField(max_length=50, null=False)
    base_price = models.IntegerField()

    @property
    def full_name(self) -> str:
        return f"{self.brand} - {self.product_type}"
    
    def __str__(self) -> str:
        return self.full_name

class Client(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.name
    
class SalesOrder(models.Model):
    IN_PROCESS = "IN PROCESS"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    ORDER_STATUS_CHOICES = {
        IN_PROCESS: "In process",
        COMPLETED: "Completed",
        CANCELED: "Canceled",
    }
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(default=datetime.now)
    products = models.ManyToManyField(Product, through="OrderItem")
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default=IN_PROCESS)

    def __str__(self):
        return f"{self.created_at.day}/{self.created_at.month} - {self.client} - {self.status}"
    

class OrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    product_price = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1, null=False)
    item_discount = models.IntegerField(default=0)
    