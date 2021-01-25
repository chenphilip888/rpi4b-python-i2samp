#!/usr/bin/python

import sys, time
import sounddevice as sd
import soundfile as sf

datafC2, fC2 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_C2.wav')
datafD2, fD2 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_D2.wav')
datafE2, fE2 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_E2.wav')
datafF2, fF2 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_F2.wav')
datafG2, fG2 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_G2.wav')
datafA2, fA2 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_A2.wav')
datafB2, fB2 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_B2.wav')
datafC3, fC3 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_C3.wav')
datafD3, fD3 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_D3.wav')
datafE3, fE3 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_E3.wav')
datafF3, fF3 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_F3.wav')
datafG3, fG3 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_G3.wav')
datafA3, fA3 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_A3.wav')
datafB3, fB3 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_B3.wav')
datafC4, fC4 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_C4.wav')
datafD4, fD4 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_D4.wav')
datafE4, fE4 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_E4.wav')
datafF4, fF4 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_F4.wav')
datafG4, fG4 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_G4.wav')
datafA4, fA4 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_A4.wav')
datafB4, fB4 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_B4.wav')
datafC5, fC5 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_C5.wav')
datafD5, fD5 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_D5.wav')
datafE5, fE5 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_E5.wav')
datafF5, fF5 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_F5.wav')
datafG5, fG5 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_G5.wav')
datafA5, fA5 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_A5.wav')
datafB5, fB5 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_B5.wav')
datafC6, fC6 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_C6.wav')
datafD6, fD6 = sf.read('/home/pi/rpi4b-python-i2samp/Piano_D6.wav')

def tone(note, duration):
    if note == 0:
        time.sleep(duration)
    else:
        if note != 0:
            sd.stop()
        if note == 1:
            sd.play(datafC4, fC4)
        elif note == 2:
            sd.play(datafD4, fD4)
        elif note == 3:
            sd.play(datafE4, fE4)
        elif note == 4:
            sd.play(datafF4, fF4)
        elif note == 5:
            sd.play(datafG4, fG4)
        elif note == 6:
            sd.play(datafA4, fA4)
        elif note == 7:
            sd.play(datafB4, fB4)
        elif note == 8:
            sd.play(datafC5, fC5)

        time.sleep(duration)

def tongsong():
    melody = [1, 1, 5, 5, 6, 6, 5, 0, 4, 4, 3, 3, 2, 2, 1, 0, 5, 5, 4, 4, 3, 3, 2, 0, 5, 5, 4, 4, 3, 3, 2, 0, 1, 1, 5, 5, 6, 6, 5, 0, 4, 4, 3, 3, 2, 2, 1, 0]
    noteDurations = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    thisNote = 0
    while thisNote < 48:
        noteDuration = 1.7 / noteDurations[thisNote];
        tone(melody[thisNote], noteDuration)
        thisNote = thisNote + 1

if __name__ == "__main__":
    tongsong()
    sys.exit()
