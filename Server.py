import socket
import sys
from thread import *


c= raw_input('ENTER T for tcp , U for UDP servers\n')
if c=='T':

    HOST = ''   # Symbolic name meaning all available interfaces
    PORT = 5558 # Arbitrary non-privileged port
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'

     

    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error , msg:
        print  'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
        
         
       


    #Start listening on socket
    print  'Socket bind complete'    
    s.listen(10)
    print 'Socket now listening'

    #Function for handling connections. This will be used to create threads
    def clientthread(conn,addr):
          #infinite loop so that function do not terminate and thread do not end.
     while 1:
            #Receiving from client
        try:
          data =conn.recv(1024)
          if not data:
               break
         
          data1,data2=data.split(',')
          data3=int(data1) + int(data2)
          reply=str(data3)
          conn.sendall(reply)
        except:
            sys.exit()
        
         
        #came out of loop
        conn.close()#fin from server
        print 'connection with ' +str(addr)+ ' closed\n'

        
       #now keep talking with the client
     
    while 1:

      #wait to accept a connection - blocking call
      
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])+'\n'
      
      #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(conn,addr[1],))
     
        


        
elif c=='U':
    
    HOST = ''   # Symbolic name meaning all available interfaces
    PORT = 6667 # Arbitrary non-privileged port
     
    # Datagram (udp) socket
    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print 'Socket created'
    except socket.error, msg :
        print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
     
     
    # Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error , msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
         
    print 'Socket bind complete'

    def clientthread(d):
          #infinite loop so that function do not terminate and thread do not end.
        while True:
             
            #Receiving from client
            data=d[0]
           
            addr=d[1]
           
            data1,data2=data.split(',')
            data3=int(data1) + int(data2)
            reply=str(data3)
            s.sendto(reply , addr)
           

    while 1:
       
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
 
          
          d =s.recvfrom(1024)
          if not d:
               break
          addr=d[1]
          print d
          start_new_thread(clientthread, (d,))
 
   
          
          
     
else:
 print 'invalid option'

