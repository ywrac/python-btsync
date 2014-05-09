#!/usr/bin/env python

import sys
from btsyncasia import BTSyncAsia as BTSync
from config import host,port,user,pswd,prefix

secret=sys.argv[1]

b=BTSync(host,port,user,pswd,prefix)

print b.register_secret(secret)
