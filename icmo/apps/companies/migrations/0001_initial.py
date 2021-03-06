# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-05 18:56
from __future__ import unicode_literals

import cloudinary.models
import dirtyfields.dirtyfields
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(max_length=150, verbose_name='Company Name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name')),
                ('website', models.URLField(blank=True, max_length=150)),
                ('address1', models.CharField(max_length=255, verbose_name='Address 1')),
                ('address2', models.CharField(blank=True, max_length=255, verbose_name='Address 2')),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(choices=[(b'', b''), (b'AL', 'Alabama'), (b'AK', 'Alaska'), (b'AB', 'Alberta'), (b'AS', 'American Samoa'), (b'AZ', 'Arizona'), (b'AR', 'Arkansas'), (b'AA', 'Armed Forces Americas'), (b'AE', 'Armed Forces Europe'), (b'AP', 'Armed Forces Pacific'), (b'BC', 'British Columbia'), (b'CA', 'California'), (b'CO', 'Colorado'), (b'CT', 'Connecticut'), (b'DE', 'Delaware'), (b'DC', 'District of Columbia'), (b'FL', 'Florida'), (b'GA', 'Georgia'), (b'GU', 'Guam'), (b'HI', 'Hawaii'), (b'ID', 'Idaho'), (b'IL', 'Illinois'), (b'IN', 'Indiana'), (b'IA', 'Iowa'), (b'KS', 'Kansas'), (b'KY', 'Kentucky'), (b'LA', 'Louisiana'), (b'ME', 'Maine'), (b'MB', 'Manitoba'), (b'MD', 'Maryland'), (b'MA', 'Massachusetts'), (b'MI', 'Michigan'), (b'MN', 'Minnesota'), (b'MS', 'Mississippi'), (b'MO', 'Missouri'), (b'MT', 'Montana'), (b'NE', 'Nebraska'), (b'NV', 'Nevada'), (b'NB', 'New Brunswick'), (b'NH', 'New Hampshire'), (b'NJ', 'New Jersey'), (b'NM', 'New Mexico'), (b'NY', 'New York'), (b'NL', 'Newfoundland and Labrador'), (b'NC', 'North Carolina'), (b'ND', 'North Dakota'), (b'MP', 'Northern Mariana Islands'), (b'NT', 'Northwest Territories'), (b'NS', 'Nova Scotia'), (b'NU', 'Nunavut'), (b'OH', 'Ohio'), (b'OK', 'Oklahoma'), (b'ON', 'Ontario'), (b'OR', 'Oregon'), (b'PA', 'Pennsylvania'), (b'PE', 'Prince Edward Island'), (b'PR', 'Puerto Rico'), (b'QC', 'Quebec'), (b'RI', 'Rhode Island'), (b'SK', 'Saskatchewan'), (b'SC', 'South Carolina'), (b'SD', 'South Dakota'), (b'TN', 'Tennessee'), (b'TX', 'Texas'), (b'UT', 'Utah'), (b'VT', 'Vermont'), (b'VI', 'Virgin Islands'), (b'VA', 'Virginia'), (b'WA', 'Washington'), (b'WV', 'West Virginia'), (b'WI', 'Wisconsin'), (b'WY', 'Wyoming'), (b'YT', 'Yukon')], max_length=2)),
                ('zip', models.CharField(max_length=12)),
                ('country', models.CharField(choices=[(b'', b''), (b'US', b'United States'), (b'CA', b'Canada')], default=b'US', max_length=3)),
                ('logo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('fiscal_year_start', models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1)),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'permissions': (('view_company', 'View company'),),
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=(b'company', b'user'))),
                ('title', models.CharField(blank=True, max_length=75)),
                ('owner', models.BooleanField(default=False)),
                ('permitted_segments_list', models.TextField(blank=True)),
            ],
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CompanyUserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name')),
                ('name', models.CharField(max_length=255)),
                ('editable', models.BooleanField(default=True, help_text=b'Some default plans should never be deleted or edited by the user')),
                ('revenue_plans', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('program_mix', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('budgets', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('performance', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('resources', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('timeline', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('task_boards', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('dashboards', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('reports', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('permissions', models.CharField(choices=[(b'none', b'None'), (b'view', b'View'), (b'change', b'Change')], default=b'none', max_length=50)),
                ('live_plan_only', models.BooleanField(default=True)),
                ('permitted_segments_list', models.TextField(blank=True, help_text=b'Restrict this group to certain segments.  Each exact segment name should be entered on a separate line.  Note, in the case that all of the segments a user has access to are not found or are inactive, users from  this group will not be able to access anything.')),
                ('publish_plans', models.BooleanField(default=False)),
                ('archive_plans', models.BooleanField(default=False)),
                ('share', models.CharField(choices=[(b'none', b'None'), (b'none', b'View'), (b'none', b'Change')], default=b'none', max_length=50)),
                ('moderate_shares', models.BooleanField(default=False)),
            ],
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CompanyUserInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('target_email', models.EmailField(max_length=255)),
                ('is_new_user', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.CharField(max_length=25, verbose_name='Application Name')),
                ('object_name', models.CharField(max_length=25, verbose_name='Object Name')),
                ('object_id', models.IntegerField(verbose_name='Object ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
        ),
    ]
