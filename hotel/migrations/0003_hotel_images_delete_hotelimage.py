# Generated by Django 4.1.1 on 2022-10-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_remove_hotel_images_hotelimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='images',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.DeleteModel(
            name='HotelImage',
        ),
    ]