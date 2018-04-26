# -*- coding:utf-8 -*-
# @Time 2018/4/13 14:44
# @Author Taste
import os

import pymysql


# models
ALARM_LEVEL = [
    (3, u'轻微'),
    (2, u'普通'),
    (1, u'严重'),
]
USER_STATUS_CHOICES = [
    ('received', u'收到'),  # 已收到告警
    ('skipped', u'被收敛'),  # 处理跳过
    ('shield', u'被屏蔽'),
    ('notified', u'已通知')
]
SOURCE = [
    ('1', u"蓝鲸"),
    ('2', u"apl")
]

# db
B_config = {
          'host': '192.168.1.182',
          'port': 3306,
          'user': 'mysql',
          'password': 'mysql',
          'db': 'bkdata_monitor_alert',
          'charset': 'utf8mb4',
          'cursorclass': pymysql.cursors.DictCursor,
          }
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),"record.log")

