# Generated by Django 4.0 on 2022-02-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_instagram_telegram_twitter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Emails',
        ),
        migrations.RemoveField(
            model_name='addresses',
            name='address_uz',
        ),
        migrations.AlterField(
            model_name='addresses',
            name='address',
            field=models.TextField(verbose_name='Адрес'),
        ),
    ]
