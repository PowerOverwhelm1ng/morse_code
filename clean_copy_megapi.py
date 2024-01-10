import RPi.GPIO as GPIO
import time
##
##
# Constants
BUZZER_PIN = 8  # GPIO pin connected to the buzzer
TEMPO = 1200

# The melody (note frequencies) and durations
# You will need to define the frequencies for N_D3, N_D4, etc. based on your requirements
melody = [N_D3, N_D3, N_D4, N_A3, 0, ...]  # Complete this list based on your melody
noteDurations = [16, 16, 8, 6, 32, ...]  # Complete this list based on your note durations

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    melody_len = len(melody)

    for thisNote in range(melody_len):
        noteDuration = TEMPO / noteDurations[thisNote]
        play_tone(BUZZER_PIN, melody[thisNote], noteDuration)
        pauseBetweenNotes = noteDuration * 1.45
        time.sleep(pauseBetweenNotes / 1000)  # Convert milliseconds to seconds

def play_tone(pin, frequency, duration):
    if frequency == 0:
        time.sleep(duration / 1000)
    else:
        buzzer = GPIO.PWM(pin, frequency)
        buzzer.start(50)  # 50% duty cycle
        time.sleep(duration / 1000)
        buzzer.stop()

if __name__ == '__main__':
    try:
        setup()
    finally:
        GPIO.cleanup()
