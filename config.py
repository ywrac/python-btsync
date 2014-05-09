import json

prefs = json.load(open('config.json'))

host = prefs['host']
port = prefs['port']
user = prefs['user']
pswd = prefs['pswd']

prefix= prefs['prefix']
