import mido
from mido import MidiFIle, MidiTrack, Message

def create_midi_file(melody, noteDurations, tempo, output_filename):
    mid = MidiFIle()
    track - MidiTrack()
    mid.tracks.append(track)

#Midi files use tempo in microseconds per beat not beats per minute the way i wrote originally
    
    microseconds_per_beat = mido.bpm2tempo(tempo)
    track.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_beat))

    for note, duration in zip(melody, noteDurations):
        #assume duration is in some unit, convert to midi
        duration_ticks = convert_duration_to_ticks(duration)
        if note == 0: #this note is a rest
            track.append(Message('note_off', note= previous_note, velocity=0, time=duration_ticks))
        else:
            track.append(Message('note_on', note= note, velocity=64, time=0))#Note start
            track.append(Message('note_off', note=note, velocity=0, time=duration_ticks))#note ends
            previous_note = note

        mid.save(output_filename)
        