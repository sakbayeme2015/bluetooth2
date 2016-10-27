#!/usr/bin/env python 

import lightblue
from signal import signal, SIGALRM , alarm
import sys

channel_status = 0
got_timeout = False
timeout = 2


if len(sys.argv) < 2:
 print "Usage : ./bluetooth_scan.py <addr>"
 exit()

def bluetooth_scan():

 def sig_alrm_handler(signum , frame):

  global got_timeout
  got_timeout = True

 signal(SIGALRM , sig_alrm_handler) 

 for channel in range(1 , 31):

  socket_object = lightblue.socket()
  got_timeout = False
  channel_status = 0

  try:
   alarm(timeout)
   socket_object.connect((sys.argv[1], channel))
   alarm(0)
   socket_object.close()
   channel_status = 1

  except IOError:
   pass

  if got_timeout == True:
   print "Channel " + str(channel) + "filtered"  
   got_timeout = False
  elif channel_status == 0:
   print "Channel " + str(channel) + "Closed"
  elif channel_status == 1:
   print "Channel " + str(channel) + "Open" 

bluetooth_scan()
 
  

 

 
