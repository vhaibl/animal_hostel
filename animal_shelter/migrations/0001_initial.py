# Generated by Django 3.1.1 on 2020-09-25 17:42

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.DecimalField(decimal_places=0, max_digits=2)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=5)),
                ('height', models.DecimalField(decimal_places=0, max_digits=2)),
                ('special', models.TextField(blank=True, null=True)),
                ('arrival', models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)])),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='animal_shelter.shelter')),
            ],
        ),
    ]