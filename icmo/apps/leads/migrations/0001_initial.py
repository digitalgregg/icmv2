# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-05 18:56
from __future__ import unicode_literals

import core.fields
import core.models
from decimal import Decimal
import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import djmoney.models.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revenues', '0001_initial'),
        ('companies', '0002_auto_20220505_2356'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name')),
                ('item_type', models.CharField(choices=[(b'category', b'Category'), (b'program', b'Program')], default=b'program', max_length=10)),
                ('touches_per_contact', models.PositiveSmallIntegerField(default=10)),
                ('touches_to_mql_conversion', models.DecimalField(decimal_places=1, default=Decimal('1'), max_digits=4, verbose_name='Touches to MQL Conversion')),
                ('mql_to_sql_conversion', models.DecimalField(decimal_places=1, default=Decimal('10'), max_digits=4, verbose_name='MQL to SQL Conversion')),
                ('sql_to_sale_conversion', models.DecimalField(decimal_places=1, default=Decimal('15'), max_digits=4, verbose_name='SQL to Sale Conversion')),
                ('cost_per_mql_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('marketing_mix', models.PositiveSmallIntegerField(default=0)),
                ('cost_per_mql', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('100'), default_currency=b'USD', max_digits=10)),
                ('marketing_mix_locked', models.BooleanField(default=False)),
                ('sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('sales', models.PositiveIntegerField(default=0, editable=False)),
                ('sales_revenue', djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', editable=False, max_digits=10, verbose_name=b'Sales Goal')),
                ('sql', models.PositiveIntegerField(default=0, editable=False)),
                ('mql', models.PositiveIntegerField(default=0, editable=False)),
                ('contacts', models.PositiveIntegerField(default=0, editable=False)),
                ('touches', models.PositiveIntegerField(default=0, editable=False)),
                ('budget_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('budget', djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=10)),
                ('fixed_budget', models.BooleanField(default=False)),
                ('cost_per_sql_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('roi', models.IntegerField(default=0, editable=False)),
                ('cost_per_sql', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', editable=False, max_digits=10)),
                ('contacts_to_mql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8, verbose_name=b'Contacts to MQL Conversion')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_last_modified', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='leads.Program')),
                ('revenue_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revenues.RevenuePlan')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='revenues.Segment')),
            ],
            bases=(core.models.DenormalizedIcmoParentsMixin, dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='program',
            unique_together=set([('slug', 'segment')]),
        ),
    ]
