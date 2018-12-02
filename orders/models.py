from django.db import models

# Create your models here.


class Food(models.Model):

    price = models.IntegerField()
    img = models.ImageField(upload_to='food_pic')
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
