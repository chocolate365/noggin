# Generated by Django 4.1.5 on 2023-03-09 03:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0005_alter_list_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="list",
            options={"ordering": ["display_order"]},
        ),
    ]
