from django.db import models

class User(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    passport = models.CharField('Пассопрт', max_length=100)
    address = models.CharField('Адресс', max_length=250)
    account_id = models.AutoField(primary_key = True)

    def get_absolute_url(self):
        return f'/account/{self.id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
