from django.db import models

# Create your models here.
class Book(models.Model):
  Book_Name = models.CharField(max_length=50)
  Author = models.CharField(max_length=50)
  Price = models.IntegerField()
  Description = models.CharField(max_length=200)

  def __str__(self):
    return self.Book_Name
  

