from django.db import models
from django_resized import ResizedImageField
from base.models import User


def product_upload(instance, filename):
    return 'product/{filename}'.format(filename=filename)


def hot_upload(instance, filename):
    return 'hot/{filename}'.format(filename=filename)


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    image = ResizedImageField(
        size=[500, 300], upload_to=product_upload, null=False)
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Hots(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    image = ResizedImageField(size=[500, 300], upload_to=hot_upload)
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
