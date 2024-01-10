from gpiozero import Buzzer
import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pin numbers for the traffic lights
red_pin = 17
yellow_pin = 27
green_pin = 22
buzzer_pin = 18  # Change this to the appropriate buzzer pin

# Set GPIO mode and pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Initialize buzzer
buzzer = Buzzer(buzzer_pin)

# Function to control the traffic lights and buzzer
def traffic_light_sequence():
    while True:
        # Red Light = Stop
        GPIO.output(red_pin, GPIO.HIGH)
        buzzer.off()  # Ensure buzzer is off
        sleep(5)  # Red light stays active for 5 seconds

        # Yellow light = Get ready!
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)
        buzzer.off()  # Ensure buzzer is off
        sleep(2)  # Yellow light stays active for 2 seconds

        # Green Light = GO!
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
        buzzer.off()  # Ensure buzzer is off
        sleep(5)  # Green light stays active for 5 seconds

        # Buzz for the last few seconds of green
        buzzer.on()
        sleep(2)  # Buzzer stays active for 2 seconds

        # Reset the light sequence to red
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.HIGH)
        buzzer.off()  # Ensure buzzer is off
        sleep(2)  # Red light stays active for 2 seconds

try:
    # Run the traffic light sequence
    traffic_light_sequence()

except KeyboardInterrupt:
    # Cleanup GPIO settings
    GPIO.cleanup()
