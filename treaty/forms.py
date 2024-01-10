from .models import Categories
from django import forms

class CategoriesForm(forms.ModelForm):
    types = [
        (6, 'На пол года'),
        (12, 'На год'),
        (24, 'На 2 года'),
        (48, 'На 4 года'),
    ]

    time_active = forms.ChoiceField(choices=types, widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Длительность'
    }))

    class Meta:
        model = Categories
        fields = ['time_active']
