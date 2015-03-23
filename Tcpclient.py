import socket
import sys
from random import randint
import time
import threading
from threading import Thread
import thread
host="172.20.10.3"           # Set the server address to variable host
port=5558             

# TCP Client Code
def sentthread(num):
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Creates a socket
    s.settimeout(20)
    s.connect((host,port))          # Connect to server address --SYN--
   
    msg1=randint(0,100) #Inclusive
    msg2=randint(0,100) #Inclusive
    msg=str(msg1)+','+str(msg2)
    
    try :
        #Set the whole string
        s.sendto(msg, (host, port))

        # receive data from client (data, addr)
        d = s.recv(1024)
        #reply = d[0]
        #addr = d[1]
        print str(msg1)+'+' +str(msg2) +'=' +str(d)+'\n'
     
    except socket.error:
        #Send failed
        print 'Send failed'
        sys.exit()

try:

    threads = []
    for i in range(10):
       t = threading.Thread(target=sentthread, args=(i,))
       threads.append(t)
       t.start()
       
        
except:
   print "Error: unable to start client thread"

