from django.db import models


class Order(models.Model):
    description = models.CharField(max_length=100)
    value = models.IntegerField()
