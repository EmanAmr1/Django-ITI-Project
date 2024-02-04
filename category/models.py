from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='category/images/', blank=True, null=True)

    def getimageurl(self):
        return f'/media/{self.image}'

    @classmethod
    def getcategory(cls):
        return [(c.id, c.name) for c in cls.objects.all()]


def __str__(self):
    return self.name+' '+self.image
