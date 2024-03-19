from django.db import models



class Products(models.Model):
    product_name = models.CharField(max_length=80)
    quantity = models.IntegerField()