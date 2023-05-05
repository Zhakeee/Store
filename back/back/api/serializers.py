from rest_framework import serializers

from .models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'price', 'year', 'image', 'configure', 'quantity']
        extra_kwargs = {'id': {'read_only': True}}
        