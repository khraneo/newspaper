# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('last_rate', models.DateTimeField(null=True, blank=True)),
                ('ccy_from', models.ForeignKey(related_name='ccy_from', to='rates.Currency')),
                ('ccy_to', models.ForeignKey(related_name='ccy_to', to='rates.Currency')),
            ],
        ),
    ]
