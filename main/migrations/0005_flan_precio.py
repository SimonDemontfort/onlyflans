# Generated by Django 5.0.6 on 2024-06-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_flan_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='precio',
            field=models.TextField(default=5000),
        ),
    ]