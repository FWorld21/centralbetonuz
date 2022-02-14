from django.db import models


class Instagram(models.Model):
    link = models.TextField(verbose_name='Ссылка на Instagram аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagram'

    def __str__(self):
        return self.link


class Telegram(models.Model):
    link = models.TextField(verbose_name='Ссылка на Telegram аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'Telegram'
        verbose_name_plural = 'Telegram'

    def __str__(self):
        return self.link


class Twitter(models.Model):
    link = models.TextField(verbose_name='Ссылка на Twitter аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'Twitter'
        verbose_name_plural = 'Twitter'

    def __str__(self):
        return self.link


class PhoneNumbers(models.Model):
    number = models.CharField(max_length=18, verbose_name='Номер')

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.number


class Addresses(models.Model):
    address = models.TextField(verbose_name='Адрес')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title
