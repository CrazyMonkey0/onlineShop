# Generated by Django 4.1.7 on 2023-03-12 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_category_alter_products_producer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='producer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.producer'),
        ),
    ]
