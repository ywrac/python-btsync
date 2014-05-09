from btsync import BTSync
import json, sys

prefs = json.load(open(config.json))

host = prefs['host']
port = prefs['port']
user = prefs['user']
pswd = prefs['pswd']

secrets=sys.argv[1]

b=BTSync(host, port, user, pswd)

for secretWithN in open(secrets):
    print b.remove_folder(secretWithN.strip())

