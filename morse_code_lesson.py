import RPi.GPIO as GPIO
import time

# Set GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the LED pins
led_pin = 17  # Example pin, change as per your setup

# Setup LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' ',  # Space between words
}

# Function to blink LED based on Morse code pattern
def blink_morse_code(message):
    for char in message:
        if char == ' ':
            time.sleep(0.5)  # Wait between words
        else:
            code = morse_code[char.upper()]
            for symbol in code:
                if symbol == '.':
                    GPIO.output(led_pin, GPIO.HIGH)
                    time.sleep(0.2)  # Dot duration
                elif symbol == '-':
                    GPIO.output(led_pin, GPIO.HIGH)
                    time.sleep(0.4)  # Dash duration
                GPIO.output(led_pin, GPIO.LOW)
                time.sleep(0.2)  # Wait between signals within a letter
            time.sleep(0.4)  # Wait between letters

# Message to be transmitted in Morse code
message = "HELLO WORLD"  # Example message

# Transmit the message in Morse code through LED
blink_morse_code(message)

# Clean up GPIO
GPIO.cleanup()
