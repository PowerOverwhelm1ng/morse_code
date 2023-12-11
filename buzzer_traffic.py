#Code for quiz buzzer
#import libs
from gpiozero import Button
from time import sleep

#buzzer variable
buzzer = Buzzer(17)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)

    