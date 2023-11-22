from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.Index()
    user_id = models.ForeignKey(Order_Details)
    order_date = models.DateTimeField()
    total_price = models.DecimalField()

    def __str__(self) -> str:
        return self.order_id