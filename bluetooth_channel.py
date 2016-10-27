#!/usr/bin/env python

import lightblue
import bluetooth
import sys

if len(sys.argv) <=1:
 print "Usage : python bluetooth_channel.py <addr>"
 exit()

def bluetooth_channel():

 bluetooth_object = bluetooth.find_service(address=sys.argv[1])
 if (len(bluetooth_object) <=1):
  print "No bluetooth found"
 else:
  for j in bluetooth_object:
   for (key, value) in j.items():
    print key + ":" + str(value)
   print ""

bluetooth_channel()
