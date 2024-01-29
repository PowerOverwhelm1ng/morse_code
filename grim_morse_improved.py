import RPi.GPIO as GPIO
import time

def setup_gpio(led_pin):
    """Initialize GPIO settings for the LED pin."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(led_pin, GPIO.OUT)

def led_control(led_pin, state):
    """Control the LED state (ON/OFF)."""
    GPIO.output(led_pin, state)

def blink_morse_code(message, led_pin=17):
    """Transmit the given message in Morse code using the specified LED pin."""
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': ' / '  # Use slash as space between words for visual clarity
    }

    dot_duration = 0.2  # Standard duration of a dot
    for char in message.upper():
        if char not in morse_code:
            print(f"Character '{char}' not in Morse code dictionary.")
            continue

        code = morse_code[char]
        for symbol in code:
            if symbol == '.':
                led_control(led_pin, GPIO.HIGH)
                time.sleep(dot_duration)  # Dot
            elif symbol == '-':
                led_control(led_pin, GPIO.LOW)
                time.sleep(dot_duration * 3)  # Dash
            led_control(led_pin, GPIO.LOW)
            time.sleep(dot_duration)  # Space between dots/dashes
        time.sleep(dot_duration * 3)  # Space between letters

    time.sleep(dot_duration * 7)  # Space between words

# Example usage
led_pin = 17  # Example pin, change as per your setup
message = "HELLO WORLD"  # Example message
setup_gpio(led_pin)
blink_morse_code(message, led_pin)
GPIO.cleanup()  # Clean up GPIO at the end
