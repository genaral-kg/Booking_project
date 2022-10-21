from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

# from account.views import send_mail
from . import views

###TODO:path('api/v1/accounts/', include('account.urls'))
urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    path('login/',views.LoginView.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
]