from django.db import models

class Products(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to= 'media/')
    rating = models.FloatField()

    def __str__(self):
        return self.name



