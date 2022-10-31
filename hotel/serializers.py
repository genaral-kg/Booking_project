from django.db.models import Avg
from rest_framework import serializers
from type.models import Type
from .models import Hotel, Favorites, Like
from rating.serializers import ReviewSerializer

# TODO: LIST_SERIALIZER
# TODO:http://localhost:8000/api/v1/hotels/
#-----------------------------------------------------------------------------------
class HotelListSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Hotel
        fields = ('title', 'type','city','price','images')

        # fields = ('title','type','price','owner','images')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr
# -----------------------------------------------------------------------------------
#TODO: DETAIL-SERIALIZER
class HotelDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    type = serializers.PrimaryKeyRelatedField(required=True,queryset=Type.objects.all())
    # review = ReviewSerializer(many=True)


    class Meta:
        model = Hotel
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['rating_count'] = instance.reviews.count()
        repr['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        # a = ReviewSerializer(instance.reviews.all(), many=True).data
        # for x in a:
        #     repr['text'] = x['text']
        return repr
#---------------------------------------------------------------------------------
class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ('owner', 'hotel')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('hotel',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['hotels'] = HotelListSerializer(instance.hotel).data
        return repr



























#TODO: COMMENT - SERIALIZER
# class CommentSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Comment
#         fields = ('id', 'body', 'hotel', 'owner')

# class FavoritesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favorites
#         fields = ('hotel',)
#
#     def to_representation(self, instance):
#         repr = super().to_representation(instance)
#         repr['hotels'] = HotelListSerializer(instance.post).data
#         return repr
