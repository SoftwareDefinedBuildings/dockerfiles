
import sys
import argparse
import subprocess

#parameters: tname, tip, tport, turl

confile="""
http 
{
  upstream {tname} 
  {
    server {tip}:{tport};
  }
  server 
  {
    server_name www.{turl};
    return 301 $scheme://{turl}$request_uri;
  }
  server 
  {
    listen 80;
    server_name {turl};
    location / 
    {
      proxy_pass http://{tname};
      proxy_set_header Host      $host;
      proxy_set_header X-Real-IP $remote_addr;
    }
  }
}
"""

parser = argparse.ArgumentParser(description='Add a vhost proxy definition to nginx')
parser.add_argument('name',help="the instance name")
parser.add_argument('port',help="the port on the instance to proxy to")
parser.add_argument('url',help="the complete hostname to listen for")
args = parser.parse_args()



