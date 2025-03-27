# Generated by Django 5.1.7 on 2025-03-27 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rental_units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beschreibung', models.TextField()),
                ('status', models.CharField(choices=[('offen', 'Offen'), ('in Bearbeitung', 'In Bearbeitung'), ('erledigt', 'Erledigt'), ('dringend', 'Dringend')], max_length=20)),
                ('erstellt_am', models.DateField()),
                ('zugewiesener_handwerker', models.CharField(max_length=255)),
                ('mietobjekt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_units.rentalunit')),
            ],
        ),
    ]
