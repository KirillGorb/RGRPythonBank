from django import forms
from .models import Account
from service.models import Service
from django.forms import  NumberInput

class ReadOnlyWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return value

class AccountForm(forms.ModelForm):
    invoice_size = forms.CharField(widget=ReadOnlyWidget)

    class Meta:
        model = Account
        fields = ['invoice_size']


class PayForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['invoice_size']

        widgets = {
            "invoice_size": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            })
        }