import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"  #ip of server
port=12344
s.connect((host,port))
print "------welcome to chat-----"
msg=raw_input("Client:")
while msg!='q':
    s.send(msg)
    data=s.recv(1024)
    print "Server: ",data
    msg=raw_input("Client: ")
s.close()
                 
