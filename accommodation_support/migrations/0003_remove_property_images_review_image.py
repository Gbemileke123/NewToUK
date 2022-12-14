# Generated by Django 4.0.5 on 2022-06-28 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation_support', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='images',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='Models id')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('value', models.IntegerField(max_length=10)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accommodation_support.property')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='Models id')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('image', models.FileField(upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation_support.property')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
