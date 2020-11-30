# Generated by Django 3.1.3 on 2020-11-30 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('coordinates', models.TextField()),
                ('country', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('coordinates', models.TextField()),
                ('image', models.TextField()),
                ('attractions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractions.city')),
            ],
        ),
    ]
