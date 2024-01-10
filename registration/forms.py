from .models import User
from django.forms import ModelForm, NumberInput, TextInput
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'passport', 'address']

        widgets = {
            "full_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "phone": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "passport": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пасспорт'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адресс'
            })
        }