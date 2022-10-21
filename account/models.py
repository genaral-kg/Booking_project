from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# #######   РЕГИСТРАЦИЯ АДМИНСКОГО ЮЗЕРА

class UserManager(BaseUserManager):
    use_in_migrations = True                ###ДЛЯ МИГРАЦИИ

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('The given email must be set!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)
    #####     СОЗДАНИЯ СУПЕРЮЗЕРА
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have status is_staff=True!')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have status is_superuser=True!')
        return self._create_user(email, password, **kwargs)

    ######   СОЗДАНИЯ ОБЫЧНОГО ЮЗЕРА - КАСТОМНОГО
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30,blank=True,null=True)                    ##НОМЕР ТЕЛЕФОНА НЕ ОБЯЗАТЕЛЬНО
    email = models.EmailField('email adddress', unique=True)                        ##ПОЧТА
    password = models.CharField(max_length=110)                                     ##PASSWORD
    activation_code = models.CharField(max_length=255, blank=True)                  ##ACTIVATION_CODE AFTER CLICK
    username = models.CharField(max_length=100, blank=True)                         ##USERNAME???
    first_name = models.CharField(max_length=100, blank=True)                       ##ИМЯ
    last_name = models.CharField(max_length=100, blank=True)                        ##ФАМИЛИЯ
    avatar = models.ImageField('Аватарка',upload_to='user_avatar/',blank=True,)                 ##АВАТАРКА
    is_active = models.BooleanField(_('active'),
                                    default=False,
                                    help_text=_(
                                        'Designates whether this user should be treted as active.'
                                        'Unselect this instead of deleting accounts.'
                                    ))

    objects = UserManager()                     ### ОБЪЕКТ ОТ КЛАССА USERMANAGER

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code