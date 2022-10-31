
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter


from type.views import TypeViewSet
from hotel.views import HotelViewSet
from city.views import CityViewSet
from rating.views import RatingViewSet
from .yasg import urlpatterns as doc_urls


router = SimpleRouter()                                              #МАРШРУТИЗАТОР
router.register('types',TypeViewSet)                       #СОЗДАЕТ ПУТЬ ДЛЯ КАТЕГОРИИ
router.register('cities',CityViewSet)
router.register('hotels',HotelViewSet)
router.register('reviews',RatingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),                                    ###ЗДЕСЬ ЗАХОДИМ НА АДМИН ПАНЕЛ
    path('api/v1/',include(router.urls)),                               ### ЗДЕСЬ РОУТЕР РАБОТАЕТ СОЗДАЕТ ПУТЬ ДЛЯ TYPES - CITIES - HOTELS
    path('api/v1/accounts/', include('account.urls')),                  ### РЕГИСТРАЦИЯ ЛОГИН ЛОГАУТ
    # path('api/v1/reserves/',include('reserve.urls')),

]
urlpatterns += doc_urls                    ### SWAGGER 💤💤💤
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)