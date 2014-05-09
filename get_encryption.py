#!/usr/bin/env python
from btsync import BTSync
from config import host,port,user,pswd
import sys


try:
    secret=sys.argv[1]
except IndexError:
    print 'Oops, something was wrong!'
    sys.exit(1)

b=BTSync(host,port,user,pswd)

print b.get_encryption(secret)
