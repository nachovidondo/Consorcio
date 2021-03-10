# Generated by Django 3.1.3 on 2021-03-09 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.CharField(max_length=50, verbose_name='Departamento PH')),
                ('porcentaje_correspondiente', models.FloatField(default=1, verbose_name='Porcentaje Correspondiente del Total')),
                ('deuda_mes', models.FloatField(verbose_name='Deuda del Mes')),
                ('total_deuda', models.FloatField(verbose_name='Deuda Total')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Edificio')),
            ],
            options={
                'verbose_name': 'Edificio',
                'verbose_name_plural': 'Edificios',
            },
        ),
        migrations.CreateModel(
            name='Expensas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expensa', models.CharField(default='Expensa', max_length=200, verbose_name='expensa')),
                ('pago_dpto', models.FloatField(blank=True, null=True, verbose_name='Monto a pagar segun PH')),
                ('expensas_puras', models.FloatField(blank=True, null=True, verbose_name='Expensas Puras')),
                ('total_ingresos', models.FloatField(blank=True, null=True, verbose_name='Total ingresos')),
                ('deuda_totales', models.FloatField(blank=True, default=None, null=True, verbose_name='Total Adeudado')),
                ('intereses_mora', models.FloatField(blank=True, null=True, verbose_name='Intereses por Mora')),
                ('materiales_limpieza', models.FloatField(blank=True, null=True, verbose_name='materiales de limpieza')),
                ('servicios_luz', models.FloatField(blank=True, null=True, verbose_name='servicios electricidad')),
                ('gastos_electricidad', models.FloatField(blank=True, null=True, verbose_name='materiales y mano obra electricidad')),
                ('gastos_pintura', models.FloatField(blank=True, null=True, verbose_name='materiales y mano obra pintura')),
                ('gastos_cerrajeria', models.FloatField(blank=True, null=True, verbose_name=' materiales y mano de obra cerrajeria')),
                ('gastos_portero_electrico', models.FloatField(blank=True, null=True, verbose_name='service portero electrico')),
                ('gastos_bomba_agua', models.FloatField(blank=True, null=True, verbose_name='service bombas de agua')),
                ('gastos_matafuegos', models.FloatField(blank=True, null=True, verbose_name=' recarga matafuegos')),
                ('gastos_accesorios', models.FloatField(blank=True, null=True, verbose_name=' gastos accesorios')),
                ('vacaciones_encargado', models.FloatField(blank=True, null=True, verbose_name=' vacaciones encargado')),
                ('reemplazo_encargado', models.FloatField(blank=True, null=True, verbose_name=' reemplazo encargado')),
                ('sueldo_administrador', models.FloatField(blank=True, null=True, verbose_name='Sueldo Administrador')),
                ('ascensores', models.FloatField(blank=True, null=True, verbose_name='Gasto Ascensores')),
                ('aportes_encargado_limpieza', models.FloatField(blank=True, null=True, verbose_name='Aportes Encargado Limpieza')),
                ('sueldo_encargado_limpieza', models.FloatField(blank=True, null=True, verbose_name='Sueldo Encargado Limpieza')),
                ('seguro_edificio', models.FloatField(blank=True, null=True, verbose_name='Seguro Edificio')),
                ('sueldo_anual_complementario', models.FloatField(blank=True, null=True, verbose_name='Sueldo Anual Complementario')),
                ('total_gastos', models.FloatField(blank=True, default=0, null=True, verbose_name='Total de Gastos (Egreso) ')),
                ('porcentaje_correspondiente_dpto', models.FloatField(blank=True, null=True, verbose_name='Porcentaje Correspondiente Departamento')),
                ('depto_ph', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administracion.departamento')),
                ('edificio_expensa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administracion.edificio', verbose_name='Edificio')),
            ],
            options={
                'verbose_name': 'Expensas',
                'verbose_name_plural': 'Expensas',
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='edificio_nombre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Administracion.edificio', verbose_name='Edificio'),
        ),
    ]
