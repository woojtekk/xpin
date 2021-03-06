#!/usr/bin/python
# -*- coding: utf-8 -*-
import time 
from datetime import datetime
import serial
import getopt
import sys
import math

xpin_buffer=128

def xpin_init_port():
  ser = serial.Serial(
	port='/dev/ttyUSB3',
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=0.10,
	xonxoff=0,
	rtscts=1)

#  ser.open()
  ser.isOpen()
  ser.flushOutput()
  ser.flushInput()
  return ser

def xpin_close_port(ser):
	ser.close()


def xpin_count(ser):
	for x in xrange(1,4):
		ser.read(xpin_buffer)

	counter=0
	tstart=time.time()

	for x in xrange(1,10):
		ss=ser.read(xpin_buffer).split("/")[0]
		counter +=float(ss[1:])

	print counter/(time.time()-tstart)


xpin=xpin_init_port()
xpin_count(xpin)


while False:
	print xpin.read(xpin_buffer)


xpin_close_port(xpin)
