from django.db import models


class Banners(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    subtitle = models.CharField(max_length=200, verbose_name='Подзаголовок', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Баннер', blank=False)

    class Meta:
        verbose_name = 'Главный баннер'
        verbose_name_plural = 'Главные баннеры'

    def __str__(self):
        return self.title


class WorkingWithUs(models.Model):
    title = models.CharField(max_length=500, verbose_name="Имя партнера", blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Лого партнёра', blank=False)

    class Meta:
        verbose_name = 'Партнёра'
        verbose_name_plural = 'Партнёры'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название', blank=False)
    new = models.TextField(verbose_name='Новость', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Фото', blank=False)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title
