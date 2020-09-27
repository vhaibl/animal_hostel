from datetime import date

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class Animal(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=120, verbose_name='Имя')  # кличка
    age = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Возвраст')  # возраст, не более 99
    weight = models.DecimalField(max_digits=5, decimal_places=3,
                                 verbose_name='Вес(кг)')  # вес до грамма, не более 99.999
    height = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Рост(см)')  # рост
    special = models.TextField(blank=True, null=True, verbose_name='Особые приметы')  # особые приметы
    arrival = models.DateField(
        validators=[MaxValueValidator(limit_value=date.today)], default=timezone.now,
        verbose_name='Дата прибытия')  # дата прибытия, не позднее сегодня
    shelter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Приют')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
