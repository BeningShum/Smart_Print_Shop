# Generated by Django 4.2.7 on 2023-11-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_alter_printers_options_alter_printers_inkvol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='note',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
