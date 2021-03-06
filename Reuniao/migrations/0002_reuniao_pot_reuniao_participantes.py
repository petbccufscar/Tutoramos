# Generated by Django 4.0.6 on 2022-07-14 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POT', '0001_initial'),
        ('Perfil', '0002_perfil_pot_perfil_user'),
        ('Reuniao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reuniao',
            name='POT',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='POT.pot'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reuniao',
            name='participantes',
            field=models.ManyToManyField(to='Perfil.perfil'),
        ),
    ]
