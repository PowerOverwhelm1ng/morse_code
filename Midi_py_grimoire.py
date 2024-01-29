import RPi.GPIO as GPIO
import time
import mido
import math

# Constants for notes
N_B0, N_C1, N_CS1, N_D1, N_DS1, N_E1, N_F1, N_FS1, N_G1, N_GS1, N_A1, N_AS1, N_B1, N_C2, N_CS2, N_D2, N_DS2, N_E2, N_F2, N_FS2, N_G2, N_GS2, N_A2, N_AS2, N_B2, N_C3, N_CS3, N_D3, N_DS3, N_E3, N_F3, N_FS3, N_G3, N_GS3, N_A3, N_AS3, N_B3, N_C4, N_CS4, N_D4, N_DS4, N_E4, N_F4, N_FS4, N_G4, N_GS4, N_A4, N_AS4, N_B4, N_C5, N_CS5, N_D5, N_DS5, N_E5, N_F5, N_FS5, N_G5, N_GS5, N_A5, N_AS5, N_B5, N_C6, N_CS6, N_D6, N_DS6, N_E6, N_F6, N_FS6, N_G6, N_GS6, N_A6, N_AS6, N_B6, N_C7, N_CS7, N_D7, N_DS7, N_E7, N_F7, N_FS7, N_G7, N_GS7, N_A7, N_AS7, N_B7, N_C8, N_CS8, N_D8, N_DS8 = (
    31, 33, 35, 37, 39, 41, 44, 46, 49, 52, 55, 58, 62, 65, 69, 73, 78, 82, 87, 93, 98, 104, 110, 117, 123, 131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247, 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880, 932, 988, 1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976, 2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951, 4186, 4435, 4699, 4978
)

# Melody and note durations arrays
melody = [N_D3, N_D3, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, ...]  # Truncated for brevity
noteDurations = [16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, ...]  # Truncated for brevity

# Constants
BUZZER_PIN = 8  # GPIO pin connected to the buzzer
TEMPO = 1200

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def play_tone(pin, frequency, duration):
    if frequency == 0:
        time.sleep(duration / 1000)
        return
    buzzer = GPIO.PWM(pin, frequency)
    buzzer.start(50)  # 50% duty cycle
    time.sleep(duration / 1000)
    buzzer.stop()

def frequency_to_midi_note_number(frequency):
    if frequency == 0:  # Rest
        return 0
    return int(round(69 + 12 * math.log2(frequency / 440.0)))

def duration_to_ticks(duration, tempo, ticks_per_beat=480):
    beat_duration = 60.0 / tempo
    note_duration = duration * beat_duration
    return int(round(note_duration * ticks_per_beat))

def create_midi_file(melody, noteDurations, tempo, output_filename):
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    microseconds_per_beat = mido.bpm2tempo(tempo)
    track.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_beat))

    for frequency, duration in zip(melody, noteDurations):
        midi_note = frequency_to_midi_note_number(frequency)
        duration_ticks = duration_to_ticks(duration, tempo)
        if midi_note == 0:
            track.append(mido.Message('note_off', time=duration_ticks))
        else:
            track.append(mido.Message('note_on', note=midi_note, velocity=64, time=0))
            track.append(mido.Message('note_off', note=midi_note, velocity=0, time=duration_ticks))

    mid.save(output_filename)

def main():
    try:
        setup()
        create_midi_file(melody, noteDurations, TEMPO, 'output.mid')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
