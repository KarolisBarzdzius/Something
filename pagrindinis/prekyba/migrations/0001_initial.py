# Generated by Django 3.0.7 on 2020-06-20 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Krepselis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vartotojo_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pardavejas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavad', models.CharField(blank=True, max_length=45, null=True, verbose_name='Pardavejo Pavadinimas')),
                ('priklauso', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=200, verbose_name='Pavadinimas')),
                ('aprasymas', models.TextField(blank=True, max_length=500, null=True, verbose_name='Aprasymas')),
                ('nuotrauka', models.ImageField(default='default.png', upload_to='prekes_nuotraukos', verbose_name='Nuotrauka')),
                ('kaina', models.FloatField(default=0, verbose_name='Vieneto kaina')),
                ('pardavejas_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prekyba.Pardavejas')),
            ],
        ),
        migrations.CreateModel(
            name='Sandelys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pridetas_kiekis', models.IntegerField(null=True, verbose_name='Prideti')),
                ('prekes_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prekyba.Preke', verbose_name='Preke')),
            ],
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perkamas_kiekis', models.IntegerField(null=True, verbose_name='Perkamu prekiu kiekis')),
                ('krepselio_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prekyba.Krepselis')),
                ('sandelio_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prekyba.Sandelys')),
            ],
        ),
        migrations.CreateModel(
            name='Profilis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuotrauka', models.ImageField(default='default.png', upload_to='profilio_nuotraukos')),
                ('adresas', models.CharField(blank=True, max_length=150, null=True, verbose_name='Adresas')),
                ('telefono_numeris', models.IntegerField(blank=True, null=True, verbose_name='Telefono numeris')),
                ('vartotojas', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Atsiliepimai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sukurta', models.DateTimeField(auto_now=True)),
                ('atsiliepimas', models.TextField(max_length=1234, verbose_name='')),
                ('prekes_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='prekyba.Preke')),
                ('vartotojas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]