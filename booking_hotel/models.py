# from django.conf import settings
# from django.db import models
# from django.contrib.auth import get_user_model
# from hotel.models import Hotel
#
#
#
#
# User = get_user_model()
#
#
# class BookingDays(models.Model):
#     booking = models.ForeignKey('Booking',related_name='booking_days', on_delete=models.CASCADE)
#     hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
#     booking_days = models.SmallIntegerField(default=1)
#
#
# class Booking(models.Model):
#     user = models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name='booking_days', on_delete=models.CASCADE)
#     hotel = models.ManyToManyField(Hotel, through=BookingDays)
#     first_name =models.CharField(max_length=40)
#     last_name =models.CharField(max_length=40)
#     phone_number = models.IntegerField(null=True)
#     email = models.EmailField('email address', null=True)
#     booked_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} {self.hotel} {self.booked_time}'