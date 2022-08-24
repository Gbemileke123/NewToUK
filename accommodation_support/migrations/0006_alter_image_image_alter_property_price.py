# Generated by Django 4.0.5 on 2022-08-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation_support', '0005_property_number_of_bathrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=65, null=True),
        ),
    ]