# Generated by Django 5.0.6 on 2024-06-12 20:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('slug', models.SlugField()),
                ('is_private', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FormPresupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('Correo', models.CharField(max_length=30)),
                ('producto', models.CharField(max_length=260)),
            ],
        ),
    ]
