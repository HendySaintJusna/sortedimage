# Generated by Django 2.1.5 on 2021-11-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_auto_20211103_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rarimage',
            name='file',
            field=models.CharField(max_length=100),
        ),
    ]
