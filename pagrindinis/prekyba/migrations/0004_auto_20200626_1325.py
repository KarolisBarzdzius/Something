# Generated by Django 3.0.7 on 2020-06-26 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prekyba', '0003_auto_20200624_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pardavejas',
            name='pavad',
            field=models.CharField(max_length=30, null=True, verbose_name='Pardavejas'),
        ),
        migrations.AlterField(
            model_name='preke',
            name='aprasymas',
            field=models.TextField(blank=True, max_length=600, null=True, verbose_name='Aprasymas'),
        ),
        migrations.AlterField(
            model_name='preke',
            name='pardavejas_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prekyba.Pardavejas'),
        ),
        migrations.AlterField(
            model_name='preke',
            name='pavadinimas',
            field=models.CharField(max_length=30, verbose_name='Pavadinimas'),
        ),
        migrations.AlterField(
            model_name='sandelys',
            name='prekes_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='prekyba.Preke', verbose_name='Preke'),
        ),
    ]
