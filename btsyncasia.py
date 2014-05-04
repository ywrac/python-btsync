from btsync import BTSync
import hashlib
import subprocess

class BTSyncAsia(BTSync):
    
    def __init__(self, host='localhost', port='14888', 
                 user='admin', pswd='password', prefix='/BTSync'):
        self.prefix=prefix
        BTSync.__init__(self,host,port,user,pswd)
    
    def register_secret(self, secret):
        dir_name = hashlib.sha256(secret).hexdigest()
        path = self.prefix + '/' + dir_name
        subprocess.call('if [ -d '+path+' ]; then exit 0; else mkdir ' + path + '; fi',shell=True)
        return self.add_folder(path,secret)
    
    def register_esecret(self, secret):
        esecret = self.get_secrets(secret)['encryption']
        self.register_secret(esecret)
