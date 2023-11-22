from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.Index()
    name = models.CharField(max_length=255)
    nr_available = models.IntegerField()
    img = models.ImageField()
    price = models.FloatField()

    def __str__(self) -> str:
        return "({}) {}".format(self.product_id, self.name)