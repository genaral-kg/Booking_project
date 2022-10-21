from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import  permissions
from . models import Type
from . import serializers



class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = serializers.TypeSerializer


    def get_permissions(self):
        if self.action in ('retrieve','list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]          ### ПОЧЕМУ ТО ЭТОТ ПУНКТ НЕ НАРБОТАЕТ НЕ МОЖЕМ СОЗДАТЬ-->TYPE

