# Generated by Django 5.1.2 on 2024-10-27 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='edicion_anterior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ediciones_posteriores', to='library.libro'),
        ),
    ]