from django.db import models
from django.db.models import Model, CASCADE


class Product(Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_length=255)
    img = models.ImageField(upload_to='')
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', CASCADE)
    company = models.ForeignKey('Company', CASCADE)

    def __str__(self):
        return self.name


class Saling(Model):
    name = models.CharField(max_length=255)
    date_from = models.DateTimeField(auto_now=False)
    date_to = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    products = models.ForeignKey('Product', CASCADE)

    def __str__(self):
        return self.name


class Saler(Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey('Product', CASCADE)
    category = models.ForeignKey('Category', CASCADE)

    def __str__(self):
        return self.name


class Category(Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Company(Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
