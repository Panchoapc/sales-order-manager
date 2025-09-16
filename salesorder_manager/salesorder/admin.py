from django.contrib import admin

# Register your models here.
from .models import SalesOrder, Client, Product, OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1
class SalesOrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    


admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(Client)
admin.site.register(Product)
