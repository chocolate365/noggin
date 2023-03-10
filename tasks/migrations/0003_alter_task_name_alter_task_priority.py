# Generated by Django 4.1.5 on 2023-02-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'First thing'), (2, 'ASAP'), (3, 'Soon'), (4, 'Whenever')], default=3),
        ),
    ]
