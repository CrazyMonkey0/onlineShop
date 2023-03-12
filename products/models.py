from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producent'
        verbose_name_plural = 'Producenci'


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, default='', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, default='', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Podkategoria'
        verbose_name_plural = 'Podkategorie'


class Products(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'products'
