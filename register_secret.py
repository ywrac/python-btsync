#!/usr/bin/env python

import sys
from btsyncasia import BTSyncAsia as BTSync

host='localhost'
port='14888'
user='admin'
pswd='password'
prefix='/Users/ywr/BTSync'

secret=sys.argv[1]

b=BTSync(host,port,user,pswd,prefix)
print b.register_secret(secret)
