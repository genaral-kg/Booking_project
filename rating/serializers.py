from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):      # это для to representation
   owner = serializers.ReadOnlyField(source='owner.email')
   # hotel = serializers.ReadOnlyField(source='hotel.title')

   class Meta:
      model = Review
      # fields = "__all__"
      exclude = ['id','hotel',]

class ReviewSerializer2(serializers.ModelSerializer):      #это для list reviews
   owner = serializers.ReadOnlyField(source='owner.email')
   hotel = serializers.ReadOnlyField(source='hotel.title')

   class Meta:
      model = Review
      fields = "__all__"

