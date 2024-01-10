from .models import Service
from django.forms import ModelForm, NumberInput, Select,ChoiceField

from enum import Enum

class Categories(Enum):
    CREDIT = 1
    CARD = 2
    DEPOSIT = 3
    MORTGAGE = 4

class ServiceForm(ModelForm):
    types = [
        ('На машину', 'На машину'),
        ('На технику', 'На технику'),
        ('На отдых', 'На отдых'),

        ('На дом', 'На дом'),
        ('На квартиру', 'На квартиру'),

        ('Драг металы', 'Драг металы'),
        ('Акции банка', 'Акции банка'),
    ]

    service = ChoiceField(choices=types, widget=Select(attrs={
        'class': 'form-control',
        'placeholder': 'Длительность'
    }))

    def get_services(self, t: Categories):
        filtered_choices = [('Лояльность', 'Лояльность')]
        if t == Categories.CREDIT:
            filtered_choices = [('На машину', 'На машину'), ('На технику', 'На технику'),('На отдых', 'На отдых')]
        elif t == Categories.DEPOSIT:
            filtered_choices = [('Драг металы', 'Драг металы'), ('Акции банка', 'Акции банка')]
        elif t == Categories.MORTGAGE:
            filtered_choices = [('На дом', 'На дом'),('На квартиру', 'На квартиру')]

        return filtered_choices

    class Meta:
        model = Service
        fields = ['price', 'service']

        widgets = {
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            })
        }
