#!/usr/bin/env python

import sys
from btsyncasia import BTSyncAsia as BTSync

host='localhost'
port='14888'
user='admin'
pswd='password'
prefix='/Users/ywr/BTSync'

secrets_file=sys.argv[1]

b=BTSync(host,port,user,pswd,prefix)

for secretWithN in open('secrets_file','r'):
    b.register_secret(secretWithN.strip())
