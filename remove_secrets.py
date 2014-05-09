from btsync import BTSync
from config import host, port, user, pswd
import sys


secrets=sys.argv[1]

b=BTSync(host, port, user, pswd)

for secretWithN in open(secrets):
    print b.remove_folder(secretWithN.strip())

