from registration.models import User
from django.forms import ModelForm, NumberInput, TextInput
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone']

        widgets = {
            "phone": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            })
        }