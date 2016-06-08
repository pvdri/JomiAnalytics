import os
import requests
import sqlite3
from models import analytics, jcanalytics
import datetime
from django.utils.dateformat import format
import time


def time_check():
    latest_entry = analytics.objects.order_by('-time')[0]
    print "Last organization data recorded into the database: " + latest_entry.org
    print "Last (clicky) time data was recorded into the database: " + latest_entry.timep
    print "Last (unix) time data was recorded into the database: " + latest_entry.time
    print "Last session ID data recorded into the database: " + latest_entry.si

    x = datetime.datetime.now()
    current_time = time.mktime(x.timetuple())
    z = (int(current_time) - int(latest_entry.time)) / (60*60*24)
    y = max(0, z+1)
    print "Acquiring data from %s day(s) ago to update database" %(y-1)
    populate(y)


def populate(y):
    for s in range (y):
        url = 'https://api.clicky.com/api/stats/4?site_id=100716069&sitekey=93c104e29de28bd9&type=visitors-list'
        date = '&date=%s-days-ago' %s
        limit = '&limit=all'
        output = '&output=json'
        total = url+date+limit+output
        print "Starting population script:  %s" %(total)
        r = requests.get(total)
        data = r.json()
        for item in data[0]['dates'][0]['items']:
            si = item["session_id"]
            ip = item["ip_address"]
            time = item["time"]
            timep = item["time_pretty"]
            if item.has_key("geolocation"):
                geol = item["geolocation"]
            else:
                geol = ""
            if item.has_key("organization"):
                org = item["organization"]
            else:
                org = ""
            add_entry(si,ip,org,time,timep,geol)
            add_jcentry(org)

def add_entry(si,ip,org,time,timep,geol):
    entry = analytics.objects.get_or_create(si=si,ip=ip,org=org,time=time,timep=timep,geol=geol)[0]
    return entry

def add_jcentry(org):
    jcentry = jcanalytics.objects.get_or_create(org=org)[0]
    return jcentry

time_check()
