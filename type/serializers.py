from rest_framework import serializers
from .models import Type

class TypeSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Type
        fields = '__all__'



