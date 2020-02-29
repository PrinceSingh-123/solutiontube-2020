from django.db import models

# Create your models here.
class ebook(models.Model):
    genres = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    desp = models.CharField(max_length=100)
    ebook = models.FileField(upload_to="../media" )
    img =  models.ImageField(upload_to="images" )

# Displaying the name of ebooks in admin page!
    def __str__(self):
        return self.title
    