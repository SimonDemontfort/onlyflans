# Generated by Django 5.0.6 on 2024-06-19 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_flan_slug_flan_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flan',
            name='precio',
        ),
    ]
