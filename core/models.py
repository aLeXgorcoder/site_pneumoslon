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
