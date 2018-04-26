# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=32, null=True, verbose_name='IP', blank=True)),
                ('alarm_type', models.CharField(max_length=100, null=True, verbose_name='\u544a\u8b66\u7c7b\u578b', blank=True)),
                ('alarm_content', models.TextField(null=True, verbose_name='\u544a\u8b66\u5185\u5bb9', blank=True)),
                ('alarm_level', models.IntegerField(default=1, verbose_name='\u544a\u8b66\u7b49\u7ea7,1\u6700\u4e25\u91cd', choices=[(3, '\u8f7b\u5fae'), (2, '\u666e\u901a'), (1, '\u4e25\u91cd')])),
                ('node_name', models.CharField(max_length=64, null=True, verbose_name='\u8282\u70b9\u540d\u79f0', blank=True)),
                ('node_type', models.CharField(max_length=64, null=True, verbose_name='\u8282\u70b9\u7c7b\u578b', blank=True)),
                ('user_status', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7528\u6237\u72b6\u6001', choices=[(b'received', '\u6536\u5230'), (b'skipped', '\u88ab\u6536\u655b'), (b'shield', '\u88ab\u5c4f\u853d'), (b'notified', '\u5df2\u901a\u77e5')])),
                ('begin_time', models.CharField(max_length=64, null=True, verbose_name='\u544a\u8b66\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('end_time', models.CharField(max_length=64, null=True, verbose_name='\u544a\u8b66\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('source', models.CharField(max_length=16, null=True, verbose_name='\u544a\u8b66\u6e90', blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
