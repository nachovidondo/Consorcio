# Generated by Django 3.1.3 on 2021-03-11 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0002_delete_expensas'),
        ('Expensas', '0006_auto_20210311_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensas',
            name='ph_dpto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PH', to='Administracion.departamento'),
        ),
    ]
