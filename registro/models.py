from django.db import models


class Category(models.Model):
    nombre = models.CharField(max_length=200)


class Spent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mount = models.IntegerField(default=0)
