import datetime
import socket

sock = socket.socket()
sock.bind(('', 80))
sock.listen(1)
conn, addr = sock.accept()
saddr = sock.getsockname()
sip, sport = saddr
ip, port = addr
print('Server IP:', sip, ':', sport)
print('Client IP:', ip, ':', port)
while True:
 data = conn.recv(1024)
 conn.send(bytes(str(datetime.datetime.now()), encoding = " utf-8 "))
 while True:
  ex = conn.recv(1024).decode("utf-8")
  if ex[0] == 'Y':
   break
  elif ex[0] == 'N':
   conn.shutdown(0)
   conn.close()
   exit(0)
 #end
conn.close()

