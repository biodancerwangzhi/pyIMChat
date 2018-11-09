import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
# queup 5 requests
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print "got a connection from %s"%str(addr)
    currentTime = time.ctime(time.time()) + "rn"
    clientsocket.close()
