# Generated by Django 4.2.7 on 2023-11-11 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0006_printers_printerstatus"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transactions",
            fields=[
                (
                    "transactionID",
                    models.CharField(max_length=64, primary_key=True, serialize=False),
                ),
                ("userID", models.CharField(max_length=64)),
                ("taskID", models.CharField(max_length=64)),
                ("money", models.FloatField()),
                ("submitTime", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WorkerInfo",
            fields=[
                (
                    "workerID",
                    models.CharField(max_length=64, primary_key=True, serialize=False),
                ),
                ("workername", models.CharField(max_length=64, unique=True)),
                ("position", models.CharField(max_length=64)),
                ("contact", models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name="tasks",
            name="money",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="tasks",
            name="submitTime",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
