# Generated by Django 4.2.8 on 2023-12-15 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Счет')),
                ('invoice_size', models.IntegerField(verbose_name='Invoice Size')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='registration.user')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
            },
        ),
    ]