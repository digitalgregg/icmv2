# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-05 18:56
from __future__ import unicode_literals

import core.fields
from decimal import Decimal
import dirtyfields.dirtyfields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HubspotCampaignToICMOCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HubspotCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hs_company_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=1024)),
                ('annualrevenue', models.IntegerField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HubspotConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('hub_id', models.CharField(help_text=b'Log into HubSpot to find your Hub ID in the upper righthand corner of the HubSpot application.', max_length=255)),
                ('access_token', models.CharField(max_length=255)),
                ('expires_at', models.DateTimeField(null=True)),
                ('refresh_token', models.CharField(max_length=255)),
                ('last_sync', models.DateTimeField(auto_now=True, null=True)),
                ('contacts_last_modified_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HubspotContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.PositiveIntegerField()),
                ('associatedcompanyid', models.CharField(blank=True, max_length=255)),
                ('current_lifecyclestage', models.CharField(max_length=255)),
                ('hs_analytics_first_url', models.URLField(max_length=2048)),
                ('hs_first_conversion_event_name', models.URLField(blank=True, max_length=2048)),
                ('hs_recent_conversion_event_name', models.URLField(blank=True, max_length=2048)),
                ('hs_analytics_source', models.CharField(max_length=255)),
                ('hs_analytics_source_data_1', models.CharField(max_length=2048)),
                ('hs_analytics_source_data_2', models.CharField(max_length=2048)),
                ('industry', models.CharField(max_length=255)),
                ('annualrevenue', models.PositiveIntegerField(blank=True, null=True)),
                ('original_source', models.CharField(default=b'Unknown', max_length=255)),
                ('original_campaign', models.CharField(default=b'Unknown', max_length=255)),
                ('conversion_event_name', models.CharField(blank=True, max_length=255)),
                ('campaign_name_guess', models.CharField(default=b'Unknown', max_length=255)),
                ('campaign_name_slug', models.CharField(max_length=255)),
                ('remote_timestamp', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HubspotContactEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateTimeField()),
                ('event_stage', models.CharField(choices=[(b'subscriber', b'Subscriber'), (b'lead', b'Lead'), (b'marketingqualifiedlead', b'Marketingqualifiedlead'), (b'salesqualifiedlead', b'Salesqualifiedlead'), (b'opportunity', b'Opportunity'), (b'customer', b'Customer')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HubspotDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_id', models.CharField(max_length=255)),
                ('contact_vid', models.CharField(blank=True, max_length=255)),
                ('hs_company_id', models.CharField(blank=True, max_length=255)),
                ('dealname', models.CharField(max_length=255)),
                ('amount_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('amount', core.fields.DefaultMoneyField(decimal_places=2, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
                ('dealstage', models.CharField(max_length=255)),
                ('dealstage_last_modified', models.DateTimeField()),
                ('closedwon_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HubspotRevenuePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('segment_mapping_field', models.CharField(choices=[(b'industry', b'Company Industry'), (b'annualrevenue', b'Company Annual Revenue')], default=b'industry', max_length=255)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HubspotRevenuePlanCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='HubspotRevenuePlanCampaignMonthPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('month', models.PositiveSmallIntegerField()),
                ('contacts', models.PositiveSmallIntegerField(default=0)),
                ('mql', models.PositiveSmallIntegerField(default=0)),
                ('sql', models.PositiveSmallIntegerField(default=0)),
                ('sales', models.PositiveSmallIntegerField(default=0)),
                ('sales_revenue_currency', djmoney.models.fields.CurrencyField(choices=[(b'USD', 'US Dollar')], default=b'USD', editable=False, max_length=3)),
                ('sales_revenue', core.fields.DefaultMoneyField(decimal_places=0, default=Decimal('0'), default_currency=b'USD', max_digits=13)),
            ],
            options={
                'ordering': ('hubspot_revenue_plan_campaign', 'month'),
            },
        ),
        migrations.CreateModel(
            name='HubspotRevenuePlanSegmentMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapping_field', models.CharField(choices=[(b'industry', b'Company Industry'), (b'annualrevenue', b'Company Annual Revenue')], max_length=255)),
                ('hs_value_1', models.CharField(blank=True, max_length=255)),
                ('hs_value_2', models.CharField(blank=True, max_length=255)),
                ('hubspot_revenue_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='segment_map', to='hubspot_icmo.HubspotRevenuePlan')),
            ],
            options={
                'ordering': ('hs_value_1',),
            },
        ),
    ]
