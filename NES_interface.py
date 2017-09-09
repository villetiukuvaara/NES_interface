#!/usr/bin/python

import wiringpi
from subprocess import call

LED = 8
BUTTON_A = 0
BUTTON_B = 2

def button_a_callback():
#    print "BTN A"
    wiringpi.digitalWrite(LED, 0)
    call("sudo reboot", shell=True)    

def button_b_callback():
#    print "BTN B"
    wiringpi.digitalWrite(LED, 0)
    call("sudo halt", shell=True)

print "Starting NES Interface"

wiringpi.wiringPiSetup()
wiringpi.pinMode(BUTTON_A, wiringpi.GPIO.INPUT)
wiringpi.pinMode(BUTTON_B, wiringpi.GPIO.INPUT)
wiringpi.pinMode(LED, wiringpi.GPIO.OUTPUT)
wiringpi.digitalWrite(LED, 1)

#wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_UP)

wiringpi.wiringPiISR(BUTTON_A, wiringpi.GPIO.INT_EDGE_BOTH, button_a_callback)
wiringpi.wiringPiISR(BUTTON_B, wiringpi.GPIO.INT_EDGE_BOTH, button_b_callback)

while True:
    wiringpi.delay(2000)
