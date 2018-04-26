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
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from common.mymako import render_mako_context, render_json
from extends import Bk_data,get_day_alarm, ratio, get_history_day_alarm, ratio_n
from account.decorators import login_exempt
from models import AlarmData


@login_exempt
def home(request):
    Bk_data.bk_data()
    today_alarm = get_day_alarm()
    day_1_alarm = get_day_alarm(1)
    alarm_ratio = ratio(today_alarm, day_1_alarm)

    history_7_alarm = get_history_day_alarm(7)
    history_30_alarm = get_history_day_alarm(30)
    ratio_7 = ratio_n(history_7_alarm, history_30_alarm)

    # data = AlarmData.objects.all().order_by("-time")
    context = {}
    # contents = []
    # for d in data:
    #     content = {}
    #     content["ip"] = d.ip
    #     content["alarm_type"] = d.alarm_type
    #     content["alarm_content"] = d.alarm_content
    #     content["begin_time"] = d.begin_time
    #     content["alarm_name"] = d.alarm_name
    #     content["source"] = d.source
    #     contents.append(content)
    context["today_alarm"] = today_alarm
    context["alarm_ratio"] = alarm_ratio
    context["history_7_alarm"] = history_7_alarm
    context["history_30_alarm"] = history_30_alarm
    context["ratio_7"] = ratio_7

    # context["alarm"] = json.dumps(contents)
    return render_mako_context(request, "/home_application/home.html", context)


@login_exempt
def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/home_base.html')


@login_exempt
def solarwinds(request):
    """receive data of solarwinds"""
    ip = request.GET.get("ip",0)
    alarm_name = request.GET.get("alarm_name",None)
    alarm_type = request.GET.get("alarm_type",None)
    alarm_content = request.GET.get("alarm_content",None)
    begin_time = request.GET.get("begin_time", None)
    monitor = AlarmData(
        ip=ip,
        alarm_type=alarm_type,
        alarm_name=alarm_name,
        alarm_content=alarm_content,
        begin_time=begin_time,
        source="2"
    )
    monitor.save()
    return render_json({"mes": "True"})


@login_exempt
def alarm_json_data(request):
    monitor = AlarmData.objects.all().order_by("-begin_time")
    context = {}
    data = []
    for d in monitor:
        content = {}
        content["ip"] = d.ip
        content["alarm_type"] = d.alarm_type
        content["alarm_content"] = d.alarm_content
        content["begin_time"] = d.begin_time
        content["alarm_name"] = d.alarm_name
        content["source"] = d.source
        data.append(content)
    context["list"] = data
    context["total"] = 21
    return HttpResponse(json.dumps(context), content_type='application/json')


@login_exempt
def alert_search(request):
    return render_mako_context(request, "/home_application/alert_search.html",)


