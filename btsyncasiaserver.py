import ssl, socket, SocketServer
from btsyncasia import BTSyncAsia

class BTSyncAsiaHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "%s wrote:" % self.client_address[0]
        print self.data
        # just send back the same data, but upper-cased
        b=BTSyncAsia('localhost','14888','admin','password','/Users/ywr/BTSync')
        r = b.register_secret( self.data )
        self.request.send( str(r) )
        
class STCPServer(SocketServer.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        # See SocketServer.TCPServer.__init__
        # (added ssl-support):
        SocketServer.BaseServer.__init__(self, server_address,
                                         RequestHandlerClass)
        self.socket = ssl.wrap_socket(socket.socket(self.address_family,self.socket_type),server_side=True,certfile="cert.pem")

        if bind_and_activate:
            self.server_bind()
            self.server_activate()
            
if __name__ == '__main__':
    server = STCPServer(('localhost',10023), BTSyncAsiaHandler)
    
    try:
        print 'server start'
        server.serve_forever()
    except KeyboardInterrupt, err:
        print 'server shutdown\n'
        server.shutdown()
        
