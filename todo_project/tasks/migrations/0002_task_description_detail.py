# Generated by Django 5.0.6 on 2024-06-26 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_detail',
            field=models.TextField(blank=True, verbose_name='Подробное описание'),
        ),
    ]
