import socket
import math


HOST = "irc.root-me.org"
PORT = 6667

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("NICK rootme\r\n".encode())
s.send("USER rootme rootme rootme :rootme\r\n".encode())
# We're receiving all msg about NICK and USER
msg = s.recv(2048).decode()
print(msg)
msg = s.recv(2048).decode()
print(msg)
msg = s.recv(2048).decode()
print(msg)
msg = s.recv(2048).decode()
print(msg)
msg = s.recv(2048).decode()
print(msg)
#         
s.send("JOIN  #root-me_challenge\r\n".encode())
# We're receiving all msg about joining
msg = s.recv(2048).decode()
print(msg)


# We're receiving and sending resp to candy
s.send("PRIVMSG candy !ep1\r\n".encode())
msg = s.recv(2048).decode()
resp = str(msg.split(":")[-1])
resp = resp.split("/")
n1 = int(resp[0])
n2 = int(resp[1])
resp = round(math.sqrt(n1)*n2,2)
        
s.send(f'PRIVMSG candy :!ep1 -rep {resp}\r\n'.encode())
msg = s.recv(2048).decode()
print(msg)
    

