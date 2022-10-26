# from rest_framework import serializers
# from .models import Booking,BookingDays
#
# class BookingDaysSerializer(serializers.ModelSerializer):
#     hotel_title = serializers.ReadOnlyField(source='hotel.title')
#
#     class Meta:
#         model = BookingDays
#         fields = ('hotel','hotel_title','booking_days')
#
#     def to_representation(self, instance):
#         repr = super().to_representation(instance)
#         repr.pop('hotel')
#         return repr
#
# class BookingSerializer(serializers.ModelSerializer):
#     hotels = BookingDaysSerializer(write_only=True, many=True)
#     user = serializers.ReadOnlyField(source='user.email')
#
#     class Meta:
#         model = Booking
#         fields = '__all__'






























    # def create(self, validated_data):
    #     hotels = validated_data.pop('hotels')
    #     request = self.context['request']
    #     user = request.user
    #     # reserve = Reserve.objects.create(status = 'open',user=user)
    #
    #     for hotel in hotels:
    #         try:
    #             ReserveDays.objects.create(reserve = reserve,
    #                                      hotel = hotel['hotel'],
    #                                    )
    #         except KeyError:
    #             ReserveDays.objects.create(reserve=reserve,
    #                                      hotel=hotel['hotel'])
    #
    #     return reserve
    #
    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     repr['hotels'] = ReserveDaysSerializer(instance.items.all(),many=True).data
    #     repr.pop('hotel')
    #     return repr