# Generated by Django 3.1.3 on 2021-03-10 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Expensas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensas',
            name='pago_dpto',
        ),
    ]