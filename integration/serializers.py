from rest_framework import serializers
from .models import Nome


class NomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nome
        fields = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']