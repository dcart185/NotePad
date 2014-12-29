# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name=b'date updated')),
                ('noteowner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name=b'date updated')),
                ('task_completed', models.BooleanField(default=False, verbose_name=b'task_completed')),
                ('note', models.ForeignKey(to='notes.Note')),
                ('task_writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
