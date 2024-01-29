import RPi.GPIO as GPIO

def main():
    try:
        setup()
        # Test play_tone with a known working frequency and duration
        print("Testing buzzer with a single tone")
        play_tone(BUZZER_PIN, 440, 500)  # A4 note for 500ms
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()
