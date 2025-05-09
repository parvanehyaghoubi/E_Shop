from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


class Listing(models.Model):

    title = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(default=0)
    qualification = RichTextField(blank=True)

    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    pinterest = models.TextField(blank=True)

    description = RichTextField(blank=True)
    information = RichTextField(blank=True)
    review = RichTextField(blank=True)

    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=0)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=0)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=0)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=0)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


