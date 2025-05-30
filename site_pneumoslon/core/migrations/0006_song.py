# Generated by Django 5.2 on 2025-05-05 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название песни')),
                ('duration', models.DurationField(verbose_name='Длительность')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='core.album', verbose_name='Альбом')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
                'ordering': ['title'],
            },
        ),
    ]
