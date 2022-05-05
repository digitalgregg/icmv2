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


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revenues', '0001_initial'),
        ('companies', '0002_auto_20220505_2356'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(max_length=150)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name')),
                ('source', models.IntegerField(choices=[(1, b'Manual'), (2, b'Salesforce'), (3, b'HubSpot')], default=1, verbose_name='Source')),
                ('jan_mql', models.IntegerField(default=0)),
                ('jan_sql', models.IntegerField(default=0)),
                ('jan_sales', models.IntegerField(default=0)),
                ('jan_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jan_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('jan_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jan_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('jan_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('jan_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('feb_mql', models.IntegerField(default=0)),
                ('feb_sql', models.IntegerField(default=0)),
                ('feb_sales', models.IntegerField(default=0)),
                ('feb_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('feb_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('feb_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('feb_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('feb_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('feb_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('mar_mql', models.IntegerField(default=0)),
                ('mar_sql', models.IntegerField(default=0)),
                ('mar_sales', models.IntegerField(default=0)),
                ('mar_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('mar_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('mar_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('mar_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('mar_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('mar_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('apr_mql', models.IntegerField(default=0)),
                ('apr_sql', models.IntegerField(default=0)),
                ('apr_sales', models.IntegerField(default=0)),
                ('apr_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('apr_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('apr_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('apr_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('apr_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('apr_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('may_mql', models.IntegerField(default=0)),
                ('may_sql', models.IntegerField(default=0)),
                ('may_sales', models.IntegerField(default=0)),
                ('may_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('may_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('may_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('may_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('may_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('may_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('jun_mql', models.IntegerField(default=0)),
                ('jun_sql', models.IntegerField(default=0)),
                ('jun_sales', models.IntegerField(default=0)),
                ('jun_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jun_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jun_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('jun_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('jun_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('jun_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('jul_mql', models.IntegerField(default=0)),
                ('jul_sql', models.IntegerField(default=0)),
                ('jul_sales', models.IntegerField(default=0)),
                ('jul_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jul_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('jul_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('jul_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('jul_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('jul_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('aug_mql', models.IntegerField(default=0)),
                ('aug_sql', models.IntegerField(default=0)),
                ('aug_sales', models.IntegerField(default=0)),
                ('aug_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('aug_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('aug_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('aug_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('aug_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('aug_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('sep_mql', models.IntegerField(default=0)),
                ('sep_sql', models.IntegerField(default=0)),
                ('sep_sales', models.IntegerField(default=0)),
                ('sep_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('sep_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('sep_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('sep_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('sep_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('sep_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('oct_mql', models.IntegerField(default=0)),
                ('oct_sql', models.IntegerField(default=0)),
                ('oct_sales', models.IntegerField(default=0)),
                ('oct_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('oct_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('oct_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('oct_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('oct_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('oct_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('nov_mql', models.IntegerField(default=0)),
                ('nov_sql', models.IntegerField(default=0)),
                ('nov_sales', models.IntegerField(default=0)),
                ('nov_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('nov_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('nov_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('nov_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('nov_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('nov_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('dec_mql', models.IntegerField(default=0)),
                ('dec_sql', models.IntegerField(default=0)),
                ('dec_sales', models.IntegerField(default=0)),
                ('dec_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('dec_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('dec_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('dec_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('dec_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('dec_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q1_mql', models.IntegerField(default=0)),
                ('q1_sql', models.IntegerField(default=0)),
                ('q1_sales', models.IntegerField(default=0)),
                ('q1_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q1_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q1_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q1_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q1_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q1_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q2_mql', models.IntegerField(default=0)),
                ('q2_sql', models.IntegerField(default=0)),
                ('q2_sales', models.IntegerField(default=0)),
                ('q2_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q2_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q2_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q2_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q2_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q2_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q3_mql', models.IntegerField(default=0)),
                ('q3_sql', models.IntegerField(default=0)),
                ('q3_sales', models.IntegerField(default=0)),
                ('q3_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q3_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q3_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q3_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q3_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q3_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q4_mql', models.IntegerField(default=0)),
                ('q4_sql', models.IntegerField(default=0)),
                ('q4_sales', models.IntegerField(default=0)),
                ('q4_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q4_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q4_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('q4_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('q4_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('q4_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('fiscal_year_mql', models.IntegerField(default=0)),
                ('fiscal_year_sql', models.IntegerField(default=0)),
                ('fiscal_year_sales', models.IntegerField(default=0)),
                ('fiscal_year_sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('fiscal_year_average_sale_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('fiscal_year_sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('fiscal_year_average_sale', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('fiscal_year_mql_to_sql_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('fiscal_year_sql_to_sale_conversion', core.fields.PercentField(decimal_places=1, default=0, max_digits=8)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_last_modified', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.Program')),
                ('revenue_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revenues.RevenuePlan')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revenues.Segment')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(core.models.DenormalizedIcmoParentsMixin, dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='campaign',
            unique_together=set([('slug', 'program')]),
        ),
    ]