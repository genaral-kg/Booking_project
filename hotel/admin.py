from django.contrib import admin

from hotel.models import Hotel

# Register your models here
# class HotelImageInLine(admin.TabularInline):
#     model = HotelImage
#     max_num = 10
#     min_num = 1
#
# @admin.register(Hotel)
# class HotelAdmin(admin.ModelAdmin):
#     inlines = [HotelImageInLine]


admin.site.register(Hotel)

