from django.db import models
from ckeditor.fields import RichTextField


class Basic(models.Model):
    title = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200, blank=True)

    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    youtube = models.TextField(blank=True)

    description = RichTextField(blank=True)

    footer = RichTextField(blank=True)

    def __str__(self):
        return self.title


