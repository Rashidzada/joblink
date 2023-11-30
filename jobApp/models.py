from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=233)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=233)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_cover_images',blank=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"


