from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Concert(models.Model):
    title = models.CharField(max_length=200, verbose_name='Навзвание концерта')
    date = models.DateField(verbose_name='Дата концерта')
    city = models.CharField(max_length=100, verbose_name='Город')
    location = models.CharField(max_length=200, verbose_name='Место проведения')
    ticket = models.URLField(verbose_name='Ссылка на покупку билетов')
    meeting = models.URLField(verbose_name='Cсылка на встречу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'
        ordering = ['-date']


class Album(models.Model):
    class ReleaseType(models.TextChoices):
        ALBUM = 'album', 'Альбом'
        SINGLE = 'single', 'Сингл'

    title = models.CharField(max_length=200, verbose_name='Название альбома')
    year = models.IntegerField(
        validators=[MinValueValidator(2010), MaxValueValidator(int(datetime.now().year))],
        default=datetime.now().year,
        verbose_name='Год релиза'
    )
    cover = models.ImageField(upload_to='albums/', verbose_name='Обложка альбома')
    release_type = models.CharField(
        max_length=10,
        choices=ReleaseType.choices,
        default=ReleaseType.ALBUM,
        verbose_name='Тип релиза'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['-year']


class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название песни')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', verbose_name='Альбом')
    duration = models.DurationField(verbose_name='Длительность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ['title']
