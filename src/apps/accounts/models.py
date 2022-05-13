from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from .managers import UserManager
from apps.core.models import *


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=50, db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.phone_number}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class TradePoint(TimestampedModel):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-id']
        verbose_name = "Торговая точка"
        verbose_name_plural = "Торговая точки"


class Visit(TimestampedModel):
    market = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)

    def __str__(self):
        return f"{self.market.title}"

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

