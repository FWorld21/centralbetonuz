# Generated by Django 4.0 on 2022-02-12 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_news_alter_workingwithus_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='keywords',
            new_name='new',
        ),
    ]
