#!/usr/bin/env python

from btsync import BTSync
from config import host,port,user,pswd

b=BTSync(host,port,user,pswd)

secrets=b.get_registerd_secrets()

for secret in secrets:
    print secret
