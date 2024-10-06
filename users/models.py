from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from blog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/avatars/', **NULLABLE, verbose_name=_('avatar'))
    phone = PhoneNumberField(**NULLABLE, verbose_name=_('phone'))
    country = models.CharField(max_length=64, **NULLABLE, verbose_name=_('country'))
    token = models.CharField(max_length=64, **NULLABLE, verbose_name=_('token'))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email
