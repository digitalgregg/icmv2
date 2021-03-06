# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-05 18:56
from __future__ import unicode_literals

import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0001_initial'),
        ('budgets', '0002_budgetlineitem_company'),
        ('resources', '0001_initial'),
        ('revenues', '0001_initial'),
        ('companies', '0002_auto_20220505_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('uuid', django_extensions.db.fields.ShortUUIDField(blank=True, db_index=True, editable=False, unique=True)),
                ('name', models.CharField(blank=True, default=b'New Task', max_length=150)),
                ('description', models.TextField(blank=True)),
                ('task_type', models.CharField(blank=True, choices=[(b'email', b'Email'), (b'email_design', b'Email Design'), (b'email_content', b'Email Content'), (b'landing_page_design', b'Landing Page Design'), (b'landing_page_content', b'Landing Page Content'), (b'content', b'Content')], max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[(b'unstarted', b'Unstarted'), (b'started', b'Started'), (b'finished', b'Finished'), (b'delivered', b'Delivered'), (b'rejected', b'Rejected'), (b'accepted', b'Accepted')], default=b'unstarted', max_length=255)),
                ('priority', models.CharField(blank=True, choices=[(b'low', b'Low'), (b'normal', b'Normal'), (b'high', b'High')], default=b'normal', max_length=255)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('budget_line_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budgets.BudgetLineItem')),
                ('gantt_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.GanttTask')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_last_modified', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.Program')),
                ('segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revenues.Segment')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TaskBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(max_length=150)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskboard_last_modified', to=settings.AUTH_USER_MODEL)),
                ('revenue_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revenues.RevenuePlan')),
            ],
            options={
                'ordering': ('-name',),
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TaskCheckListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('uuid', django_extensions.db.fields.ShortUUIDField(blank=True, db_index=True, editable=False, unique=True)),
                ('name', models.CharField(max_length=2048)),
                ('completed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklist', to='task_boards.Task')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', django_extensions.db.fields.ShortUUIDField(blank=True, db_index=True, editable=False, unique=True)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='task_boards.Task')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('action', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='task_boards.Task')),
            ],
            options={
                'ordering': ('-modified',),
            },
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('uuid', django_extensions.db.fields.ShortUUIDField(blank=True, db_index=True, editable=False)),
                ('name', models.CharField(default=b'New Task List', max_length=150)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasklist_last_modified', to=settings.AUTH_USER_MODEL)),
                ('task_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_boards.TaskBoard')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TaskTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', django_extensions.db.fields.ShortUUIDField(blank=True, db_index=True, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('task_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_boards.TaskBoard')),
            ],
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[(b'owner', b'Owner'), (b'approver', b'Approver'), (b'reviewer', b'Reviewer')], max_length=255)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_users', to='task_boards.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='task_boards.TaskTag'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_boards.TaskBoard'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_boards.TaskList'),
        ),
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(through='task_boards.TaskUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='tasktag',
            unique_together=set([('task_board', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='taskboard',
            unique_together=set([('slug', 'revenue_plan')]),
        ),
    ]
