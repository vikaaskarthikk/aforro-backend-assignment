from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    def __str__(self): return self.name

class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ['store', 'product']
