from gps import *
import time
import serial

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
    port = "/dev/ttyUSB0"
    rate = 9600
    s1 = serial.Serial(port, rate)
    s1.flushInput()
    if s1.inWaiting()>0:
        inputValue = s1.readline()
        return inputValue

def data_sender(line):
    port = "/dev/ttyUSB0"
    rate = 9600
    s1 = serial.Serial(port, rate)
    s1.write(line)


