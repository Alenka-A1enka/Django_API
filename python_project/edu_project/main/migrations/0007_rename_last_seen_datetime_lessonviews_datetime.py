# Generated by Django 4.2.1 on 2023-09-28 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_datetime_lessonviews_last_seen_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonviews',
            old_name='last_seen_datetime',
            new_name='datetime',
        ),
    ]
