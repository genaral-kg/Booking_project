# from django.shortcuts import render
# from rest_framework.generics import CreateAPIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions
# from .models import Booking
# from .serializers import BookingSerializer
# # Create your views here.
#
# class CreateBookingView(CreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class UserBookingList(APIView):
#
#     def get(self,request):
#         user = request.user
#         booking = user.booking_days.all()                                                                    #orders = Order.objects.filter(user=user)
#         serializer = BookingSerializer(reserve, many=True)
#         return Response(serializer.data, status=200)

