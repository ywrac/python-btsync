#!/usr/bin/env python

import sys
from btsyncasia import BTSyncAsia as BTSync
from config import host,port,user,pswd,prefix

secrets_file=sys.argv[1]

b=BTSync(host,port,user,pswd,prefix)

for secretWithN in open(secrets_file,'r'):
    print b.register_secret(secretWithN.strip())
