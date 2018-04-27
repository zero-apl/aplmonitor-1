import pymysql
conn = pymysql.connect(host='172.18.0.201', user = "root", passwd="root", db="aplmonitor", port=3306, charset="utf8")
cur = conn.cursor()
sql = "select * from home_application_alarmdata where ip = '192.168.1.170';"

try:
   cur.execute(sql)
   results = cur.fetchall()
   for row in results:
      ip = row[1]
      alarm_name = row[2]
      alarm_type = row[3]
      alarm_content = row[4]
      begin_time = row[5]

      print "ip=%s,alarm_name=%s,alarm_type=%s,alarm_content=%s,begin_time=%s" % \
             (ip, alarm_name, alarm_type, alarm_content, begin_time )
except:
   print "Error: unable to fecth data"
cur.close()
conn.close()


