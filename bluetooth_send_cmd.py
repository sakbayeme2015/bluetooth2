#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bluetooth
import time


def prog():

 socket_object = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
 socket_object.connect(("3A:65:2B:13:9E:5E" , 1))
 socket_object.send('AT+CPBR=1\r')   #read phonebook entry 
 time.sleep(1)
 socket_object.send(chr(26))
 contents = socket_object.recv(1024)
 print contents
 socket_object.close()

prog()
