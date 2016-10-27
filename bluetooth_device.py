#!/usr/bin/env python

import bluetooth

def bluetooth_devices():

 bluetooth_object = bluetooth.discover_devices(lookup_names = True)

 for addr , name in bluetooth_object:
  
  print '%s: %s' % (addr,name)

 
  
bluetooth_devices()
