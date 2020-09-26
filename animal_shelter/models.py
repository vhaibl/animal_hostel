from datetime import date

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

#
# class Shelter(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name


class Animal(models.Model):
    name = models.CharField(max_length=120)  # кличка
    age = models.DecimalField(max_digits=2, decimal_places=0)  # возраст, не более 99
    weight = models.DecimalField(max_digits=5, decimal_places=3)  # вес до грамма, не более 99.999
    height = models.DecimalField(max_digits=2, decimal_places=0)  # рост
    special = models.TextField(blank=True, null=True)  # особые приметы
    arrival = models.DateField(
        validators=[MaxValueValidator(limit_value=date.today)])  # дата прибытия, не позднее сегодня
    # shelter = models.ForeignKey('Shelter', related_name='animals', on_delete=models.CASCADE)
    shelter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
