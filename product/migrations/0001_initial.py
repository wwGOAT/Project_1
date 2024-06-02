# Generated by Django 5.0.6 on 2024-06-02 19:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CategoryProduct',
                'verbose_name_plural': 'CategoryProducts',
            },
        ),
        migrations.CreateModel(
            name='ColorProducstModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ColorProduct',
                'verbose_name_plural': 'ColorProducts',
            },
        ),
        migrations.CreateModel(
            name='ManufactureProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ManufactureProduct',
                'verbose_name_plural': 'ManufactureProducts',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ProductTag',
                'verbose_name_plural': 'ProductTags',
            },
        ),
        migrations.CreateModel(
            name='ProducuctsChoisSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ProducuctsChoisSize',
                'verbose_name_plural': 'ProducuctsChoisSizes',
            },
        ),
        migrations.CreateModel(
            name='ProducstModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='product')),
                ('image2', models.ImageField(null=True, upload_to='product')),
                ('reyting', models.FloatField(default=0.0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dicount', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('code', models.CharField(blank=True, max_length=8, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='products', to='product.categoryproductsmodel')),
                ('color', models.ManyToManyField(related_name='products', to='product.colorproducstmodel')),
                ('manufacture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.manufactureproductsmodel')),
                ('tags', models.ManyToManyField(related_name='products', to='product.producttagmodel')),
                ('sizes', models.ManyToManyField(related_name='products', to='product.producuctschoissizemodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='CommentsProductsModle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='product.producstmodel')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]