# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-05 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyUserNotificationSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('notification_type', models.CharField(choices=[(b'task_overdue', b'Task Overdue')], max_length=255)),
                ('frequency', models.CharField(editable=False, max_length=255)),
                ('params', models.TextField(blank=True)),
                ('params_display', models.TextField(blank=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.CompanyUser')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
    ]
