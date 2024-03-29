# Generated by Django 4.0.6 on 2022-08-10 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POT', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='POT',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='potianos', to='POT.pot'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
