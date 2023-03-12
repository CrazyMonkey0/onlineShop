# Generated by Django 4.1.7 on 2023-03-12 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='producer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.producer'),
        ),
    ]
