"""
Copyright (c) 2013, Regents of the University of California
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions 
are met:

 - Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
 - Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import uuid
import time
import random
import psycopg2

#This is ripped from my unit test code I wrote a while back, kinda kludgey but hey
# -MPA
class Bootstrapper(object):

    DB_USER="archiver"
    DB_PASSWD="password"
    DB_NAME="archiver"
    TURL="http://127.0.0.1:8079"
    subkey='8AUYLo3KpQgw5eH1QVu7WuVFunittest9001'
    
    def delete_user(self):
        con = psycopg2.connect("port=5432 host=127.0.0.1 dbname={} user={} password={}".format(self.DB_NAME,self.DB_USER,self.DB_PASSWD))
        cur = con.cursor()
        cur.execute("DELETE FROM stream WHERE subscription_id = (SELECT id FROM subscription WHERE owner_id=9001 LIMIT 1)")
        cur.execute("DELETE FROM subscription WHERE owner_id = 9001")
        cur.execute("DELETE FROM auth_user WHERE id = 9001")
        con.commit()
        cur.close()
        con.close()
        
    def make_user(self):
        """
        Mostly copied from the twisted archiver plugin
        """
        #It's over 9000 so that should be ok.
        uid=9001
        #make a user:
        uqry = """INSERT INTO auth_user VALUES ({id}, 'auto{id}','','','',
                  'pbkdf2_sha256$10000$QWwLmgl17URJ$cZ258SNnRqER3V1e4HMOMTMyjUZI0fAmlJr/elMLS14=',
                  't','t','t','2013-10-08 22:21:35.566316-07','2013-10-08 22:01:57.650245-07')""".format(id=uid)
        guuid = str(uuid.uuid1())
        sqry = """INSERT INTO subscription (uuid, resource, key, public, description, url, owner_id) VALUES ('{uuid}','/+','{subkey}','t','test2','',{uid});"""
        sqry = sqry.format(uid=uid,uuid=guuid,subkey=self.subkey)
        
        #I don't care about async in tests    
        con = psycopg2.connect("port=5432 host=127.0.0.1 dbname={} user={} password={}".format(self.DB_NAME,self.DB_USER,self.DB_PASSWD))
        cur = con.cursor()
        cur.execute(uqry)
        cur.execute(sqry)
        con.commit()
        cur.close()
        con.close()
        
b = Bootstrapper()
b.make_user()
        
            
