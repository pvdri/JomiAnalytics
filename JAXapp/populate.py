import os
import requests
import sqlite3
from models import analytics, jcanalytics


def populate():
    url = 'https://api.clicky.com/api/stats/4?site_id=100716069&sitekey=93c104e29de28bd9&type=visitors-list'
    date = '&date=last-30-days'
    limit = '&limit=all'
    output = '&output=json'
    total = url+date+limit+output
    r = requests.get(total)
    print(total)
    data = r.json()
    # html = []
    for item in data[0]['dates'][0]['items']:
        si = item["session_id"]
        ip = item["ip_address"]
        time = item["time"]
        timep = item["time_pretty"]
        # geol = item["geolocation"]
        # org = item["organization"]
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

print "Starting population script..."
populate()
