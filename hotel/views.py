from django.shortcuts import render
from rest_framework import permissions, response, generics
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from rating.serializers import ReviewSerializer
from hotel.models import Hotel

from . import serializers
from .permissions import IsAuthor
# Create your views here.


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.HotelListSerializer
        return serializers.HotelDetailSerializer

    def get_permissions(self):
        if self.action in ('update','partial_update','destroy'):
            return [permissions.IsAuthenticated(),IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(['GET','POST'], detail=True)
    def reviews(self,request,pk):
        hotel = self.get_object()
        if request.method == 'GET':
            reviews = hotel.reviews.all()
            serializer = ReviewSerializer(reviews,many=True)
            return response.Response(serializer.data, status=200)
        if hotel.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, hotel=hotel)
        return response.Response(serializer.data, status=201)

    # /posts/<id>/comments/
    # @action(['GET'], detail=True)
    # def comments(self, request, pk):
    #     post = self.get_object()
    #     comments = post.comments.all()
    #     serializer = serializers.CommentSerializer(comments, many=True)
    #     return Response(serializer.data, status=200)

    # @action(['POST'], detail=True)
    # def favorite_action(self, request, pk):
    #     hotel = self.get_object()
    #     user = request.user
    #     if user.favorites.filter(hotel=hotel).exists():
    #         user.favorites.filter(hotel=hotel).delete()
    #         return Response('Deleted from Favorites!', status=204)
    #     Favorites.objects.create(owner=user, post=post)
    #     return Response('Added to Favorites!', status=201)



##todo:CREATE COMMENT VIEWS

# class CommentListCreateView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
# # todo: DETAILVIEW ---> COMMENT
# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
#
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [permissions.AllowAny()]
#         return [permissions.IsAuthenticated(), IsAuthor()]
























