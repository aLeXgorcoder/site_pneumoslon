# Generated by Django 5.2 on 2025-05-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='age_limit',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Возрастное ограничение'),
        ),
    ]
