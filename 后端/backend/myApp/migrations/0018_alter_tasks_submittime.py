# Generated by Django 4.2.7 on 2023-11-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0017_alter_tasks_submittime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="submitTime",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
