from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Products, Hots


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('pk', 'user_id', 'category', 'name', 'image',
                  'quantity', 'amount', 'description')


class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['category', 'name', 'image',
                  'quantity', 'amount', 'description']


class CreateHotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hots
        fields = ['user', 'name', 'image',
                  'quantity', 'amount', 'description']


class HotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hots
        fields = ['name', 'image', 'quantity', 'amount', 'description']
