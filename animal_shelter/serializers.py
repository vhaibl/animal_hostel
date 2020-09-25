from rest_framework import serializers

from animal_shelter.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('name', 'age', 'weight', 'height', 'special', 'arrival', 'shelter_id')


from datetime import date

# from django.core.validators import MaxValueValidator
# from rest_framework import serializers
#
# from .models import Animal
#
#
# class AnimalSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=120)
#     age = serializers.DecimalField(max_digits=2, decimal_places=0)
#     weight = serializers.DecimalField(max_digits=5, decimal_places=3)  # вес
#     height = serializers.DecimalField(max_digits=2, decimal_places=0)  # рост
#     special = serializers.CharField(allow_blank=True)  # особые приметы
#     arrival = serializers.DateField(validators=[MaxValueValidator(limit_value=date.today)])  # дата прибытия
#     shelter_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Animal.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.weight = validated_data.get('weight', instance.weight)
#         instance.height = validated_data.get('height', instance.height)
#         instance.special = validated_data.get('special', instance.special)
#         instance.arrival = validated_data.get('arrival', instance.arrival)
#         instance.shelter_id = validated_data.get('shelter_id', instance.shelter_id)
#         instance.save()
#         return instance
