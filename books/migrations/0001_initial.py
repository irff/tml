# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('year_published', models.DateField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('language', models.CharField(choices=[('EN', 'English'), ('ID', 'Indonesian')], default='EN', max_length=2)),
                ('authors', models.ManyToManyField(to='books.Author')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
