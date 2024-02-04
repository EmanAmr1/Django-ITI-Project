from django.db import models
from category.models import *
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='product/images/', blank=True, null=True)
    category=models.ForeignKey(Category,blank=True,null=True,on_delete=models.CASCADE)

    @classmethod
    def product_list(self):
        return self.objects.all()

    @classmethod
    def product_detailes(cls, proid):
        return cls.objects.get(id=proid)

    def getimageurl(self):
        return f'/media/{self.image}'


def __str__(self):
    return self.name+' '+self.image
