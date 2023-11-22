from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nr_available = models.IntegerField()
    img = models.ImageField()
    price = models.FloatField()

    def __str__(self) -> str:
        return "({}) {}".format(self.product_id, self.name)
    
#Order table - contains order_ID(primary key), user_ID(foreign key-Order_Details table), order_date, total_price
class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(Order_Details, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    total_price = models.DecimalField()

    def __str__(self) -> str:
        return self.order_id

## This is class for Order-Details table. It connects to Orders, Product tables/classes
class Order_Details(models.Model):
    o_details_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self) -> str :
        return self.o_details_id

