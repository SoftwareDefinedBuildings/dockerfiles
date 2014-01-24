#!/usr/bin/env python
import sys
import argparse
import subprocess
import json
import os
import os.path
import pymongo

client = pymongo.MongoClient()
db = client.proxies

#parameters: tname, tip, tport, turl


upstream="""
  upstream {tname}-{tport} 
  {{
    server {tip}:{tport};
  }}
"""
confile="""
  server 
  {{
    server_name www.{turl};
    return 301 $scheme://{turl}$request_uri;
  }}
  server 
  {{
    listen 80;
    server_name {turl};
    location / 
    {{
      proxy_pass http://{tname}-{tport};
      proxy_set_header Host      $host;
      proxy_set_header X-Real-IP $remote_addr;
    }}
  }}

"""

parser = argparse.ArgumentParser(description='Add a vhost proxy definition to nginx')
parser.add_argument('--add', help="add a new record (requires name, port and url)", action="store_true")
parser.add_argument("--remove", help="remove a record. Required the url", action="store_true")
parser.add_argument('--list', help="list all records as they were prior to any actions", action="store_true")
parser.add_argument('--name',help="the instance name")
parser.add_argument('--port',help="the port on the instance to proxy to")
parser.add_argument('--url',help="the complete hostname to listen for")
parser.add_argument('--regen',help="remove and regenerate all automatic records", action="store_const",const=True,default=False)
args = parser.parse_args()

def gen_config(record):
    doc = subprocess.check_output(["docker", "inspect", record["name"]])
    if len(doc) == 0:
        print "No such instance found: ",record["name"]
        sys.exit(1)
    doc = json.loads(doc)[0]
    ip = doc["NetworkSettings"]["IPAddress"]
    
    of = open("/etc/nginx/sites-enabled/auto-serve-{}.conf".format(record["url"]),"w")
    of.write(confile.format(tname=record["name"], tport=record["port"], turl=record["url"], tip=ip))
    of.close()
    of = open("/etc/nginx/sites-enabled/auto-upstream-{}-{}.conf".format(record["name"],record["port"]),"w")
    of.write(upstream.format(tname=record["name"], tport=record["port"], turl=record["url"], tip=ip))
    of.close()

def del_configs():
    fpath = "/etc/nginx/sites-enabled"
    for f in os.listdir(fpath):
        if f.startswith("auto-"):
            fname = os.path.join(fpath, f)
            os.unlink(fname)

if args.list:
   for i in db.entities.find():
        print "RECORD: {url} to docker://{name}:{port}".format(**i)
         
if args.add:    
    if args.name is None or args.port is None or args.url is None:
        print "You need the name, port and URL to add a record"
        sys.exit(1)
            
    #Try update existing config for that name:
    existing = db.entities.find_one({"url":args.url, "port":args.port})
    record = {"url":args.url, "port":args.port, "name":args.name}
    if existing is not None:
        record["_id"] = existing["_id"]
    db.entities.save(record)
    gen_config(record)

if args.remove:
    if args.url is None:
        print "You need the URL to remove a record"
        sys.exit(1)
    db.entities.remove({"url":args.url})
            
if args.regen:
    del_configs()
    for i in db.entities.find():
        print "adding: {url} to docker://{name}:{port}".format(**i)
        gen_config(i)

op = subprocess.check_output(["/usr/sbin/nginx", "-t"])
op = subprocess.check_output(["service", "nginx","reload"])




