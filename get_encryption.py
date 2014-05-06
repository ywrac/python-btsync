#!/usr/bin/env python

import sys
from btsync import BTSync

host='localhost'
port='14888'
user='admin'
pswd='password'

try:
    secret=sys.argv[1]
except IndexError:
    print 'Oops, something was wrong!'
    sys.exit(1)

b=BTSync(host,port,user,pswd)

print b.get_encryption(secret)
