from django.db import models

# Create your models here.

#Order table - contains order_ID(primary key), user_ID(foreign key-Order_Details table), order_date, total_price
class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(Order_Details, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    total_price = models.DecimalField()

    def __str__(self) -> str:
        return self.order_id