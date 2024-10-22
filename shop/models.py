from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField()


    def __str__(self):
        return self.title