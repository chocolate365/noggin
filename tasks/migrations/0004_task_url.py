# Generated by Django 4.1.5 on 2023-02-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_name_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]