# Generated by Django 4.2.7 on 2023-11-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0008_remove_transactions_taskid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactions",
            name="transName",
            field=models.CharField(default="1", max_length=64),
            preserve_default=False,
        ),
    ]
