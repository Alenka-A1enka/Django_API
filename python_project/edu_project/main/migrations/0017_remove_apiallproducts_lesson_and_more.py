# Generated by Django 4.2.1 on 2023-09-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_access_user_alter_access_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiallproducts',
            name='lesson',
        ),
        migrations.AddField(
            model_name='apiallproducts',
            name='lesson_name',
            field=models.CharField(default='Без названия', max_length=250, verbose_name='Название урока'),
        ),
        migrations.AddField(
            model_name='apiallproducts',
            name='lesson_url',
            field=models.URLField(default='http://...', verbose_name='Ссылка на видео'),
        ),
    ]
