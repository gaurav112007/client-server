import socket
import sys
host="127.0.0.1"
port=12344
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
print"Listening on...."
conn,addr=s.accept()
print "connection from:"+str(addr)
print "------welcome to chat----"

while True:
    data=conn.recv(1024)

    if not data:
        break
    print "Client :",str(data)
    rep=raw_input("Server:")
    conn.send(rep)
conn.close()
                 
                 
