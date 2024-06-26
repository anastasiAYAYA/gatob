# Generated by Django 4.2.13 on 2024-06-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0038_remove_creatives_performance_remove_creatives_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conductor',
            name='performance',
        ),
        migrations.CreateModel(
            name='PerformanceConductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiche.creatives')),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiche.performance')),
            ],
            options={
                'verbose_name_plural': 'Performance Conductors',
            },
        ),
    ]
