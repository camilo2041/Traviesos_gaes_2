# Generated by Django 4.2.4 on 2023-09-06 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_citas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_mascota', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Nombre mascota',
                'verbose_name_plural': 'Nombre mascotas',
                'db_table': 'Mascota',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='agendar_cita',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_citas.mascota'),
        ),
    ]