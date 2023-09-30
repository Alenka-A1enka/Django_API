# Generated by Django 4.2.1 on 2023-09-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_lessonviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonviews',
            old_name='datetime',
            new_name='last_seen_datetime',
        ),
        migrations.AddField(
            model_name='lessonviews',
            name='viewing_duration',
            field=models.PositiveIntegerField(default=400, verbose_name='Длительность просмотра'),
            preserve_default=False,
        ),
    ]
