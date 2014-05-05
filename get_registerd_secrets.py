#!/usr/local/bin/python

from btsync import BTSync

host='localhost'
port='14888'
user='admin'
pswd='password'

b=BTSync(host,port,user,pswd)

secrets=b.get_registerd_secrets()

for secret in secrets:
    print secret
