from rest_framework import serializers

from animal_shelter.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('name', 'age', 'weight', 'height', 'special', 'arrival', 'shelter', 'id')


class AnimalSerializerLimited(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('name', 'special')
