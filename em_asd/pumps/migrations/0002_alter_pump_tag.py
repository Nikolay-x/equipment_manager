# Generated by Django 4.1.3 on 2022-11-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pump',
            name='tag',
            field=models.CharField(max_length=30, unique=True, verbose_name='Tag'),
        ),
    ]
