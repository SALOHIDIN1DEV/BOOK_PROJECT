from django.db import models
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    descrption = models.TextField()
    isbn = models.CharField(max_length=14)
    cover_pic = models.ImageField(upload_to="book_pics")

    def __str__(self):
        return self.title

