# Generated by Django 4.2.1 on 2023-09-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_apiallproducts_lesson_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='APICurrentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(default='Без названия', max_length=250, verbose_name='Название урока')),
                ('lesson_url', models.URLField(default='http://...', verbose_name='Ссылка на видео')),
                ('status', models.BooleanField(default=False, verbose_name='Статус просмотра')),
                ('viewing_time_in_seconds', models.PositiveIntegerField(verbose_name='Время просмотра видео')),
                ('datetime', models.DateTimeField(verbose_name='Дата последнего просмотра видео')),
            ],
        ),
    ]
