from django.db import models


class Objects(models.Model):
    little_desc = models.CharField(max_length=300, verbose_name='Краткое описание', blank=False, unique=True)
    full_desc = models.TextField(verbose_name='Полное описание', blank=False)
    address = models.CharField(max_length=300, verbose_name='Адрес', blank=False)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.little_desc


class ObjectImages(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, verbose_name='Для объекта', default=None)
    pic = models.ImageField(upload_to='media', verbose_name='Картинка')

    def __str__(self):
        return self.object.little_desc

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title
