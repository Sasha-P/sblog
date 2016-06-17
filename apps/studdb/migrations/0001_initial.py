# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Group name')),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('firs_name', models.CharField(max_length=30, verbose_name='First name')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Patronymic')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studdb.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name_plural': 'Students',
                'verbose_name': 'Student',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='studdb.Student', verbose_name='Monitor'),
        ),
    ]
