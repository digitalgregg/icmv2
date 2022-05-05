# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-05 18:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revenues', '0001_initial'),
        ('budgets', '0002_budgetlineitem_company'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetlineitem',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='budgetlineitem_last_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='budgetlineitem',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='budgets.BudgetLineItem'),
        ),
        migrations.AddField(
            model_name='budgetlineitem',
            name='program',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.Program'),
        ),
        migrations.AddField(
            model_name='budgetlineitem',
            name='revenue_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revenues.RevenuePlan'),
        ),
        migrations.AddField(
            model_name='budgetlineitem',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revenues.Segment'),
        ),
        migrations.AlterUniqueTogether(
            name='budgetlineitem',
            unique_together=set([('slug', 'segment')]),
        ),
    ]
