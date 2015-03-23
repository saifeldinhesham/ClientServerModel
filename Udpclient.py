import socket   #for sockets
import sys  #for exit
from random import randint
import time
from thread import *
import threading
from threading import Thread, current_thread

host ="172.20.10.3";
port = 6667;

def sentthread(num):
 
# create dgram udp socket
  
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
      print 'Failed to create socket'
      sys.exit()
 
  
 

    msg1=randint(0,100) #Inclusive
    msg2=randint(0,100) #Inclusive
    msg=str(msg1)+','+str(msg2)
    
     
  #Set the whole string

    s.sendto(msg, (host, port))
             
# receive data from client (data, addr)
  
    d = s.recvfrom(1024)
    reply = d[0]
    print str(msg1)+'+' +str(msg2) +'=' +str(reply)+'\n'
    
try:
    
    threads = []
    for i in range(7):
          t = threading.Thread(target=sentthread, args=(i,))
          threads.append(t)
          t.start()
except:
    print'Error: unable to start client thread'
    



