# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitordata',
            name='alarm_name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u544a\u8b66\u540d\u79f0', blank=True),
        ),
    ]
