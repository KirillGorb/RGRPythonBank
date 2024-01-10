from registration.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    account_id = models.AutoField(primary_key=True, verbose_name='Счет')
    invoice_size = models.IntegerField(verbose_name='Invoice Size')

    def get_absolute_url(self):
        return f'/account/{self.account_id}'

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
