from django.db import models

# Create your models here.
class Ratings(models.Model):
    product = models.CharField(max_length = 255)
    description = models.TextField()
