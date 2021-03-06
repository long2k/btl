# Generated by Django 4.0.3 on 2022-03-04 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.CharField(default=1, max_length=25),
        ),
        migrations.AddField(
            model_name='item',
            name='create_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default=1, max_length=500),
        ),
        migrations.AddField(
            model_name='item',
            name='name_book',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='type_book',
            field=models.CharField(default=1, max_length=255),
        ),
    ]
