#!/usr/bin/env python

import pymongo
import sys
import subprocess
import modprox
import argparse
from collections import namedtuple 

client = pymongo.MongoClient()
proxdb = client.proxies
rapidb = client.rapid

parser = argparse.ArgumentParser(description='Stop and delete a service')
parser.add_argument('urlprefix', help="the url prefix to delete")
args = parser.parse_args()
url = args.urlprefix+".rapid.cal-sdb.org"
print "Looking for",url
srv = rapidb.services.find_one({"url":args.urlprefix})
if srv is None:
    print "No such service found"
    sys.exit(1)
if "containerid" in srv:
    print "Container launched, stopping"
    did = srv["containerid"]
    rv = subprocess.call(["docker","stop",did])
    assert rv == 0

print "Removing proxy definiton"
modprox.call(namedtuple("args",["remove","url","list","regen","add"])(True,url,False,True,False))

print "Removing service descriptor"
rapidb.services.remove({"_id":srv["_id"]})

print "Done"
   
    
    
