# Generated by Django 4.0 on 2022-02-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_banners'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingWithUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Имя партнера')),
                ('img', models.ImageField(upload_to='media', verbose_name='Лого партнёра')),
            ],
        ),
        migrations.AlterField(
            model_name='banners',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Баннер'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='Подзаголовок'),
        ),
    ]
