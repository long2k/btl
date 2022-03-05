from django.db import models

# Create your models here.
class Item(models.Model):
    name_book = models.CharField(max_length=255, default=1)
    type_book = models.CharField(max_length=255, default=1)
    author = models.CharField(max_length=25, default=1)
    price = models.IntegerField(default=1)
    description = models.CharField(max_length=500, default=1)
    status = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Items'