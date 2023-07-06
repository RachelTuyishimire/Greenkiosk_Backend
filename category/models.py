from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "category"
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

