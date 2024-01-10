from django import forms
from .models import Account

class ReadOnlyWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return value

class AccountForm(forms.ModelForm):
    invoice_size = forms.CharField(widget=ReadOnlyWidget)

    class Meta:
        model = Account
        fields = ['invoice_size']