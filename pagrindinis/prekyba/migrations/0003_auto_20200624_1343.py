# Generated by Django 3.0.7 on 2020-06-24 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prekyba', '0002_auto_20200624_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandelys',
            name='prekes_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prekyba.Preke', verbose_name='Preke'),
        ),
    ]