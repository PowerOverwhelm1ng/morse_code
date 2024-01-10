#import libraries and explain what libraries are
import RPi.GPIO as GPIO
import time

#Define GPIO pin numbers for the traffic lights may have to change pins to handle buzzer wiring

red_pin = 17
yellow_pin = 27
green_pin = 22

#Set GPIO mode and pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

#FUNCTION to control the traffic lights

def traffic_light_sequence():
    while True:
        #Red Light = Stop
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(5) #red light stays active for 4 seconds

        #Yellow light = Get ready!
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)
        time.sleep(2) #yellow light stays active for two seconds

        #Green Light = GO!
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(5) #Green light stays active for 5 seconds

        #RESET THE LIGHT SEQUENCE TO RED
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(2) #red light stays active for 2

try:
    #run the traffic light sequence
    traffic_light_sequence()

except KeyboardInterrupt:
    #cleanup gpio settings
    GPIO.cleanup()


