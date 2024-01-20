import RPi.GPIO as GPIO
import time
import mido
import math

# Your existing code (notes definition, constants, setup, and play_tone functions)...
#notes
N_B0 = 31
N_C1 = 33
N_CS1 = 35
N_D1 = 37
N_DS1=39
N_E1 = 41
N_F1 = 44
N_FS1 = 46
N_G1= 49
N_GS1=52
N_A1 =55
N_AS1=58
N_B1=62
N_C2= 65
N_CS2=69
N_D2=73
N_DS2= 78
N_E2 =82
N_F2 =87
N_FS2=93
N_G2 =98
N_GS2=104
N_A2 =110
N_AS2=117
N_B2 =123
N_C3 =131
N_CS3=139
N_D3 =147
N_DS3=156
N_E3 =165
N_F3 =175
N_FS3=185
N_G3 =196
N_GS3 =208
N_A3=220
N_AS3=233
N_B3=247
N_C4=262
N_CS4=277
N_D4=294
N_DS4=311
N_E4=330
N_F4=349
N_FS4=370
N_G4=392
N_GS4=415
N_A4=440
N_AS4=466
N_B4=494
N_C5=523
N_CS5=554
N_D5=587
N_DS5=622
N_E5=659
N_F5=698
N_FS5=740
N_G5 =784
N_GS5=831
N_A5 =880
N_AS5=932
N_B5=988
N_C6=1047
N_CS6=1109
N_D6=1175
N_DS6=1245
N_E6=1319
N_F6=1397
N_FS6=1480
N_G6=1568
N_GS6=1661
N_A6=1760
N_AS6=1865
N_B6=1976
N_C7=2093
N_CS7=2217
N_D7=2349
N_DS7=2489
N_E7=2637
N_F7=2794
N_FS7=2960
N_G7 = 3136
N_GS7 = 3322
N_A7 = 3520
N_AS7= 3729
N_B7 =3951
N_C8=4186
N_CS8=4435
N_D8=4699
N_DS8=4978
#Melody ARRAY
melody = [N_D3, N_D3, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_C3, N_C3, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_B2, N_B2, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_AS2, N_AS2, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_D3, N_D3, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_C3, N_C3, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_B2, N_B2, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_AS2, N_AS2, N_D4, N_A3, 0, N_GS3, N_G3, N_F3, N_D3, N_F3, N_G3, N_D4, N_D4, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_C4, N_C4, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_B3, N_B3, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_AS3, N_AS3, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_D4, N_D4, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_C4, N_C4, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_B3, N_B3, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_AS3, N_AS3, N_D5, N_A4, 0, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, N_F4, N_F4, N_F4, N_F4, N_F4, N_D4, N_D4, N_D4, N_F4, N_F4, N_F4, N_G4, N_GS4, N_G4, N_F4, N_D4, N_F4, N_G4, 0, N_F4, N_F4, N_F4, N_G4, N_GS4, N_A4, N_C5, N_A4, N_D5, N_D5, N_D5, N_A4, N_D5, N_C5, N_F4, N_F4, N_F4, N_F4, N_F4, N_D4, N_D4, N_D4, N_F4, N_F4, N_F4, N_F4, N_D4, N_F4, N_E4, N_D4, N_C4, 0, N_G4, N_E4, N_D4, N_D4, N_D4, N_D4, N_F3, N_G3, N_AS3, N_C4, N_D4, N_F4, N_C5, 0, N_F4, N_D4, N_F4, N_G4, N_GS4, N_G4, N_F4, N_D4, N_GS4, N_G4, N_F4, N_D4, N_F4, N_F4, N_F4, N_GS4, N_A4, N_C5, N_A4, N_GS4, N_G4, N_F4, N_D4, N_E4, N_F4, N_G4, N_A4, N_C5, N_CS5, N_GS4, N_GS4, N_G4, N_F4, N_G4, N_F3, N_G3, N_A3, N_F4, N_E4, N_D4, N_E4, N_F4, N_G4, N_E4, N_A4, N_A4, N_G4, N_F4, N_DS4, N_CS4, N_DS4, 0, N_F4, N_D4, N_F4, N_G4, N_GS4, N_G4, N_F4, N_D4, N_GS4, N_G4, N_F4, N_D4, N_F4, N_F4, N_F4, N_GS4, N_A4, N_C5, N_A4, N_GS4, N_G4, N_F4, N_D4, N_E4, N_F4, N_G4, N_A4, N_C5, N_CS5, N_GS4, N_GS4, N_G4, N_F4, N_G4, N_F3, N_G3, N_A3, N_F4, N_E4, N_D4, N_E4, N_F4, N_G4, N_E4, N_A4, N_A4, N_G4, N_F4, N_DS4, N_CS4, N_DS4, 
]
#noteDurations Array
noteDurations = [
  16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 16, 16, 8, 6, 32, 8, 8, 8, 16, 16, 16, 8, 16, 8, 8, 8, 8, 4, 16, 8, 16, 8, 8, 8, 16, 16, 16, 16, 16, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16, 16, 2, 8, 16, 8, 8, 8, 8, 4, 16, 8, 16, 8, 8, 8, 8, 8, 16, 8, 16, 8, 8, 8, 8, 8, 8, 8, 16, 8, 15, 8, 8, 2, 3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 8, 2, 16, 8, 16, 8, 16, 16, 16, 16, 16, 16, 8, 8, 8, 8,  8, 8, 16, 16, 16, 2, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 2, 8, 8, 8, 8, 2, 2, 3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 8, 2, 16, 8, 16, 8, 16, 16, 16, 16, 16, 16, 8, 8, 8, 8,  8, 8, 16, 16, 16, 2, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 2, 8, 8, 8, 8, 2, 1]  #duration array
#CONSTANTS
BUZZER_PIN = 8  # GPIO pin connected to the buzzer
TEMPO = 1200

#SETUP
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    melody_len = len(melody)

    for thisNote in range(melody_len):
        noteDuration = TEMPO / noteDurations[thisNote]
        play_tone(BUZZER_PIN, melody[thisNote], noteDuration)
        pauseBetweenNotes = noteDuration * 1.45
        time.sleep(pauseBetweenNotes / 1000)  # Convert milliseconds to seconds
#PLAYTONE
def play_tone(pin, frequency, duration):
    if frequency == 0:
        time.sleep(duration / 1000)
    else:
        buzzer = GPIO.PWM(pin, frequency)
        buzzer.start(50)  # 50% duty cycle
        time.sleep(duration / 1000)
        buzzer.stop()

# Add a function to map frequencies to MIDI note numbers
def frequency_to_midi_note_number(frequency):
    if frequency == 0:  # Rest
        return 0
    return int(round(69 + 12 * math.log2(frequency / 440.0)))

# Add a function to convert durations to MIDI ticks
def duration_to_ticks(duration, tempo, ticks_per_beat=480):
    beat_duration = 60.0 / tempo  # Duration of one beat in seconds
    note_duration = duration * beat_duration  # Note duration in seconds
    return int(round(note_duration * ticks_per_beat))

# Function to create the MIDI file
def create_midi_file(melody, noteDurations, tempo, output_filename):
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    # Set MIDI file tempo
    microseconds_per_beat = mido.bpm2tempo(tempo)
    track.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_beat))

    for frequency, duration in zip(melody, noteDurations):
        midi_note = frequency_to_midi_note_number(frequency)
        duration_ticks = duration_to_ticks(duration, tempo)

        if midi_note == 0:  # Rest
            track.append(mido.Message('note_off', time=duration_ticks))
        else:
            track.append(mido.Message('note_on', note=midi_note, velocity=64, time=0))  # Note start
            track.append(mido.Message('note_off', note=midi_note, velocity=0, time=duration_ticks))  # Note end

    mid.save(output_filename)

def main():
    try:
        setup()
        create_midi_file(melody, noteDurations, TEMPO, 'output.mid')
        # You can add more logic here if needed
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle exceptions if necessary
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

# Example usage
create_midi_file(melody, noteDurations, TEMPO, 'output.mid')