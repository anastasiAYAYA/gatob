# Generated by Django 4.2.13 on 2024-05-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0004_alter_performance_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]