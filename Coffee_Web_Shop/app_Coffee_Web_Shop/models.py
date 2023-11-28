from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nr_available = models.IntegerField(default=0)
    img = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField(max_length=5000, blank=True, default="")

    def __str__(self) -> str:
        return "({}) {}".format(self.product_id, self.name)
    
#Order table - contains order_ID(primary key), user_ID(foreign key-Order_Details table), order_date, total_price
class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=datetime.datetime.now())
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    
    def __str__(self) -> str:
        return self.order_id

## This is class for Order-Details table. It connects to Orders, Product tables/classes
class Order_Detail(models.Model):
    o_details_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0)

    def __str__(self) -> str :
        return self.o_details_id
    

