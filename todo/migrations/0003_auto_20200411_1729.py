# Generated by Django 3.0.5 on 2020-04-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200411_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_time',
            field=models.DateTimeField(blank=True, verbose_name='Deadline'),
        ),
    ]