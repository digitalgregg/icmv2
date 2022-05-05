# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-05 18:56
from __future__ import unicode_literals

import core.fields
from decimal import Decimal
import dirtyfields.dirtyfields
from django.db import migrations, models
import django_extensions.db.fields
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name')),
                ('item_type', models.CharField(choices=[(b'category', b'Category'), (b'program', b'Program'), (b'custom', b'Custom')], default=b'category', max_length=10)),
                ('automatic_distribution', models.BooleanField(default=True)),
                ('jan_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('feb_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jan_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('feb_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('mar_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('mar_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('apr_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('may_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('apr_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('may_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jun_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jun_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jul_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('aug_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jul_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('aug_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('sep_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('sep_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('oct_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('nov_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('oct_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('nov_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('dec_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jan_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('dec_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jan_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('feb_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('mar_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('feb_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('mar_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('apr_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('may_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('apr_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('may_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jun_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jul_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jun_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jul_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('aug_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('sep_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('aug_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('sep_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('oct_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('oct_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('nov_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('dec_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('nov_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('dec_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jan_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('feb_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jan_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('mar_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('feb_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('mar_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('apr_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('apr_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('may_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jun_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('may_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jul_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jun_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('jul_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('aug_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('aug_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('sep_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('oct_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('sep_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('nov_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('oct_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('nov_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('dec_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q1_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('dec_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q1_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q1_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q1_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q1_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q2_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q1_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q2_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q2_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q2_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q2_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q2_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q3_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q3_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q3_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q3_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q3_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q4_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q3_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q4_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('q4_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q4_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q4_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('fiscal_year_actual_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q4_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('fiscal_year_actual', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('fiscal_year_plan_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('fiscal_year_variance_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('fiscal_year_plan', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('fiscal_year_variance', core.fields.DecimalMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=15)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
