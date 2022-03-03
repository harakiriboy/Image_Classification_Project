from django.db import models


# Create your models here.

class ImageDB(models.Model):
    pathh = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.address} - {self.balance}'

# Create your models here.