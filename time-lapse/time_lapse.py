#!/usr/bin/env python
import picamera
import time
from time import sleep
from fractions import Fraction

#with picamera.PiCamera() as camera:
#    camera.resolution = (1280, 720)
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800
#    camera.framerate = Fraction(1, 6)
#    camera.shutter_speed = 6000000
#    camera.exposure_mode = 'off'
#    camera.iso = 800
#    camera.hflip = True
#    camera.vflip = True
    # Give the camera a good long time to measure AWB
    # (you may wish to use fixed AWB instead)
#    sleep(10)
    # Finally, capture an image with a 6s exposure. Due
    # to mode switching on the still port, this will take
    # longer than 6 seconds
#    camera.capture('test1.jpg', quality=100)


with picamera.PiCamera() as camera:
    #camera.resolution = (1280, 720)
    camera.resolution = (1920, 1080)
    camera.start_preview()
    camera.hflip = True
    camera.vflip = True
    time.sleep(3)
    for filename in camera.capture_continuous('pics/{counter:04d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(30) # wait 5 minutes
        #time.sleep(10) # wait 5 minutes
