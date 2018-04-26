# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.db import models

from constant import ALARM_LEVEL,USER_STATUS_CHOICES,SOURCE


class ModelBase(models.Model):
    @property
    def resource(self):
        return Resource.objects.get(id=self.resource_id)


class Resource(models.Model):
    inner_ip = models.CharField(u"内网IP", max_length=32, blank=True, null=True)
    outer_ip = models.CharField(u"外网IP", max_length=32, blank=True, null=True)
    host_name = models.CharField(u"主机/节点名", max_length=64, blank=True, null=True)
    moudule = models.CharField(u"模块名", max_length=64, blank=True, null=True)
    status = models.CharField(u"主机状态", max_length=16, blank=True, null=True)
    request_id = models.CharField(u"请求id", max_length=64, blank=True, null=True)


class AlarmData(ModelBase):
    ip = models.CharField(u"IP", max_length=32, blank=True, null=True)
    alarm_name = models.CharField(u"告警名称", max_length=100, blank=True, null=True)
    alarm_type = models.CharField(u"告警类型", max_length=100, blank=True, null=True)
    alarm_content = models.TextField(u"告警内容", blank=True, null=True)
    alarm_level = models.IntegerField(u"告警等级,1最严重", default=1,
                                      choices=ALARM_LEVEL)
    node_name = models.CharField(u"节点名称", max_length=64, blank=True, null=True)
    node_type = models.CharField(u"节点类型", max_length=64, blank=True, null=True)
    user_status = models.CharField(u"用户状态", max_length=32,
                                   blank=True, null=True,choices=USER_STATUS_CHOICES)
    begin_time = models.CharField(u"告警开始时间", max_length=64, blank=True, null=True)
    end_time = models.CharField(u"告警结束时间", max_length=64, blank=True, null=True)
    source = models.CharField(u"告警源", max_length=16, blank=True, null=True, choices=SOURCE)
    time = models.DateTimeField(u"时间", auto_now_add=True)
    data = models.DateField(u"日期", auto_now_add=True)
    resource_id = models.IntegerField(u"对应资源", blank=True, null=True)


class MonitorCpu(ModelBase):
    ip = models.CharField(u"IP", max_length=32, blank=True, null=True)
    cpu_rate = models.CharField(u"cpu使用率", max_length=32, blank=True, null=True)
    time = models.CharField(u"时间", max_length=32, blank=True, null=True)





