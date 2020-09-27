from django import forms

from .models import Animal

class NewAnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ('name', 'age', 'special', 'weight', 'height')
