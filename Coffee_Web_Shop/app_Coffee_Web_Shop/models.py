from django.db import models

# Create your models here.




## This is class for Order-Details table. It connects to Orders, Product tables/classes
class Order_Details(models.Model):
    o_details_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True)

    def __str__(self) -> str :
        return self.o_details_id

