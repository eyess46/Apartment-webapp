# Generated by Django 4.2.2 on 2023-07-15 21:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.CharField(max_length=900)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=5000000)),
                ('property_type', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=500)),
                ('area_lenght', models.CharField(max_length=500)),
                ('beds', models.CharField(max_length=500)),
                ('baths', models.CharField(max_length=500)),
                ('garage', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Seravice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000000)),
                ('details', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('Properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.properties')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
