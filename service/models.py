from django.db import models

class Service(models.Model):
    service = models.CharField('Услуга', max_length=100)
    price = models.IntegerField('Цена')
    yearly_percent = models.FloatField('Годовой процент')

    def get_absolute_url(self):
        return f'/account/{self.id}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
