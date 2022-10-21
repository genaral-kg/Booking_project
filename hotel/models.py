from django.db import models

from type.models import Type
from django.contrib.auth import get_user_model

from city.models import City

User = get_user_model()


# TODO: HOTEL - CREATE FROM MODELS

class Hotel(models.Model):
    owner = models.ForeignKey(User, on_delete= models.RESTRICT,
                              related_name= 'hotels')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(Type,
                                 on_delete=models.SET_NULL,null=True,   # КОГДА УДАЛИМ КАТЕГОРИЮ НЕ УДАЛЯЕТСЯ ОТЕЛЬ
                                 related_name='hotels')               # ЗА МЕСТУ КАТЕГОРИИ СТОИТ null
    images = models.ImageField(upload_to ='images')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='hotels', null=True)
    class Meta:
        ordering = ['title']


    def __str__(self):
        return f'{self.title} - {self.type} - booking for one day {self.price}$'

# TODO:COMMENTS !!!
# class Comment(models.Model):
#     owner = models.ForeignKey('auth.User', related_name='comments',
#                               on_delete=models.CASCADE)
#     hotel = models.ForeignKey(Hotel, related_name='comments',
#                              on_delete=models.CASCADE)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.owner} -> {self.hotel} -> {self.created_at}'
#
#     class Meta:
#         verbose_name = 'Comment'
#         verbose_name_plural = 'Comments'






# TODO:ФАВОРИТЫ
# TODO: ЛАЙКИ
# TODO:РЕЙТИНГ
 #  ФАВОРИТЫ ЮЗЕРА ТОЛЬКО ОПРЕДЕЛЕННОГО
# class Favorites(models.Model):
#     owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,
#                              related_name='favorites')
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
#                              related_name='favorites')
#
#     class Meta:
#         unique_together = ['owner', 'hotel']



