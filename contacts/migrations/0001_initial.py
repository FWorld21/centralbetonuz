# Generated by Django 4.0 on 2022-02-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Адрес (Рус)')),
                ('address_uz', models.TextField(verbose_name='Адрес (Узб)')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Email адрес',
                'verbose_name_plural': 'Email адреса',
            },
        ),
        migrations.CreateModel(
            name='MetaTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('keywords', models.TextField(verbose_name='Keywords (Через запятую/Предложением)')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Мета тег',
                'verbose_name_plural': 'Мета теги',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=18, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Номера телефонов',
            },
        ),
    ]