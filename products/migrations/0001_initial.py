# Generated by Django 5.0.2 on 2024-03-02 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('inventory', models.PositiveIntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'db_table': 'gallery',
            },
        ),
    ]
