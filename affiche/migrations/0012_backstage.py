# Generated by Django 4.2.13 on 2024-05-23 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0011_rename_background_performance_background1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backstage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('date', models.DateField()),
                ('video', models.FileField(upload_to='backstage/')),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiche.performance')),
            ],
            options={
                'verbose_name_plural': 'Backstage',
            },
        ),
    ]
