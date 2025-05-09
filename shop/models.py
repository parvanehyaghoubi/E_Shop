from django.db import models


class Shop(models.Model):

    title = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(default=0)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
