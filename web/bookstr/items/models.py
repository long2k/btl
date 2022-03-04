from django.db import models

# Create your models here.
TYPE_BOOK_CHOICES = (
    ('H', 'History'),
    ('C', 'Classic '),
    ('Ho', 'Horror '),
    ('M', 'Memoir'),
    ('R', 'Romance'),

)
class Item(models.Model):
    id = models.AutoField(primary_key= True),
    name_book = models.CharField(),
    type_book = models.CharField(max_length=2, choices=TYPE_BOOK_CHOICES),
    author = models.CharField(max_length= 25),
    price = models.IntegerField(),
    description = models.CharField(max_length= 500),
    status =  models.BooleanField(default = False),
    create_at = models.DateField(auto_now_add= True),