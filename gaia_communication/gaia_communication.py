from gps import *
import time
import serial

s1 = None
NUMBER_OF_TRIES = 3

def check_serial():
    if(s1 is None):
        return False
    return s1.isOpen()
    

def open_serial_port():
    # !/usr/bin/env/python
    port = "/dev/ttyUSB0"
    rate = 9600
    tries = 0
    while(check_serial() != True):
        if(tries > NUMBER_OF_TRIES):
            tries += tries
            print("ERROR: could not open serial port", port)
            return False 
        time.sleep(0.05)
        # -*- coding: utf-8 -*-
        s1 = serial.Serial(port, rate)
    return True

def gps_data():
    # ! /usr/bin/python

    gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)
    # '\t' = TAB to try and output the data in columns.

    lat = 0
    lon = 0

    while(lat == 0 and lon == 0):
        report = gpsd.next()
        if report['class'] == 'TPV':

            lat = getattr(report, 'lat', 0.0)
            lon = getattr(report, 'lon', 0.0)
            # print(getattr(report,'epv','nan'),"\t")
            # print(getattr(report,'ept','nan'),"\t",)
            speed = getattr(report, 'speed', 'nan')

    return (lat, lon, speed)

def data_reciver():
    s1.flushInput()
    if s1.inWaiting()>0:
        inputValue = s1.readline()
        return inputValue

def data_sender(line):
    s1.write(line)


