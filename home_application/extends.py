# -*- coding:utf-8 -*-
# @Time 2018/4/13 15:55
# @Author Taste
from __future__ import division
import json
import datetime
import urllib

import pymysql
import requests

from constant import B_config, DIR
from models import AlarmData


class Bk_data:
    ip = None

    @classmethod
    def ip_affirm(cls):
        if not cls.ip:
            try:
                with open(DIR, "r") as f:
                    cls.ip = f.readlines()[-1]
            except:
                pass

        if not cls.ip:
            cls.ip = 0

    @classmethod
    def bk_data(cls):
        """"""
        cls.ip_affirm()
        # print cls.ip
        db = pymysql.connect(**B_config)
        try:
            with db.cursor() as cursor:
                sql = "SELECT ip,alarm_type,raw,level,begin_time,end_time,id,alarm_content FROM ja_alarm_alarminstance WHERE id>%d" %int(cls.ip)
                cursor.execute(sql)
                result = cursor.fetchall()
                db.commit()
        except:
            print "failed to connect to databases"
        else:
            for i in result:
                content = json.loads(i["alarm_content"])
                monitor = AlarmData(
                    ip=i["ip"],
                    alarm_type=i["alarm_type"],
                    alarm_content=i["raw"],
                    alarm_level=i["level"],
                    begin_time=i["begin_time"],
                    end_time=i["end_time"],
                    alarm_name=content["source_name"]+u"告警",
                    source="1"
                )
                monitor.save()
                cls.ip = str(i["id"])
                with open(DIR, "w") as f:
                        f.write(str(cls.ip))

        finally:
            db.close()


# def cpu_load(request):
#     bk_token = request.COOKIES.get("bk_token")
#     headers = { "Cookie":"bk_token=O1cDvajF46p-rHZ7lRFYs3UeSrjXiHvAGQQJ9OLUPHc",
#                 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#     payload = {"time_range_banner":"1","host_id":"192.168.1.183|0","index_id":"7","dimension_field_value":""}
#     r = requests.get("http://paas.blueking.com/o/bk_monitor/2/bp/graph/point/",params=payload,headers=headers)
#     try:
#         a = json.loads(r.text)
#     except:
#         pass
#     else:
#         print len(a["data"]["data"]["series"][0]["x_axis_list"])
#         print len(a["data"]["data"]["series"][0]["delay_info"])


# alarm amount
def get_day_alarm(day=0):
    today = datetime.date.today()
    one_day = datetime.timedelta(days=day)
    num = AlarmData.objects.filter(data=today - one_day).count()
    return num


def get_history_day_alarm(day):
    return sum([get_day_alarm(i) for i in xrange(day)])


def ratio(now, before):
    if before > 0:
        if now > before:
            rat = "+%d" % (((now-before) / before)*100)+"%"
        elif before > now & now != 0:
            rat = "-%d" % (((before-now) / before)*100)+"%"
        else:
            rat = "+0%"
    else:
        rat = "+0%"
    return rat


def ratio_n(date1, date2):
    return "%.2f" % (date1/date2 * 100)
