from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField()
    cover = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
