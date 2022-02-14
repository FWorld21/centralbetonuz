from django.db import models
from django.urls import reverse
from .ru_to_eng import translate


class Products(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название', blank=False)
    little_desc = models.CharField(max_length=300, verbose_name='Краткое описание', blank=False)
    full_desc = models.TextField(verbose_name='Полное описание', blank=False)
    pic = models.ImageField(upload_to='media', verbose_name='Картинка')
    price = models.CharField(max_length=100, verbose_name='Цена', blank=False)
    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('product', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title
