from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='book_posters/', null=True, blank=True)