# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_monitordata_alarm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitordata',
            name='source',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='\u544a\u8b66\u6e90', choices=[(b'1', '\u84dd\u9cb8'), (b'2', 'apl')]),
        ),
    ]
