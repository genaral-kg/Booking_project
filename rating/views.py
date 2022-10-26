from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import  Review
from . import serializers

class RatingViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer2

    def get_permissions(self):
        if self.action in ('retrieve','list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]