from rest_framework import serializers
from .models import StoreApi


class StoreApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreApi
        fields = '__all__'
