from django.db import models
from django.utils import timezone
from registration.models import User
from service.models import Service
from datetime import timedelta

class Categories(models.Model):
    categorie = models.CharField('Категория', max_length=100)
    time_active = models.IntegerField('Время действия', blank=True, null=True)
    service_id = models.OneToOneField(Service, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/treaty/{self.id}'

    def save(self, *args, **kwargs):
        if self.time_active is not None:
            self.time_active = self.time_active
        super(Categories, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Treatys(models.Model):
    data_start = models.DateTimeField('Дата начала', default=timezone.now)
    data_end = models.DateTimeField('Дата окончания', blank=True, null=True)
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.OneToOneField(Categories, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.data_end is None and self.service_id.time_active is not None:
            self.data_end = self.data_start + timedelta(days=30 * self.service_id.time_active)
        super(Treatys, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
