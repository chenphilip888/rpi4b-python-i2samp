#!/usr/bin/python

import tty, sys, termios, time
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

class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

def test():
    while True:
        with ReadChar() as rc:
            char = rc
            sd.stop()
        if char == 'z':
            sd.play(datafC2, fC2)
        elif char == 'x':
            sd.play(datafD2, fD2)
        elif char == 'c':
            sd.play(datafE2, fE2)
        elif char == 'v':
            sd.play(datafF2, fF2)
        elif char == 'b':
            sd.play(datafG2, fG2)
        elif char == 'n':
            sd.play(datafA2, fA2)
        elif char == 'm':
            sd.play(datafB2, fB2)
        elif char == ',':
            sd.play(datafC3, fC3)
        elif char == '.':
            sd.play(datafD3, fD3)
        elif char == 'a':
            sd.play(datafC3, fC3)
        elif char == 's':
            sd.play(datafD3, fD3)
        elif char == 'd':
            sd.play(datafE3, fE3)
        elif char == 'f':
            sd.play(datafF3, fF3)
        elif char == 'g':
            sd.play(datafG3, fG3)
        elif char == 'h':
            sd.play(datafA3, fA3)
        elif char == 'j':
            sd.play(datafB3, fB3)
        elif char == 'k':
            sd.play(datafC4, fC4)
        elif char == 'l':
            sd.play(datafD4, fD4)
        elif char == 'q':
            sd.play(datafC4, fC4)
        elif char == 'w':
            sd.play(datafD4, fD4)
        elif char == 'e':
            sd.play(datafE4, fE4)
        elif char == 'r':
            sd.play(datafF4, fF4)
        elif char == 't':
            sd.play(datafG4, fG4)
        elif char == 'y':
            sd.play(datafA4, fA4)
        elif char == 'u':
            sd.play(datafB4, fB4)
        elif char == 'i':
            sd.play(datafC5, fC5)
        elif char == 'o': 
            sd.play(datafD5, fD5)
        elif char == '1':
            sd.play(datafC5, fC5)
        elif char == '2':
            sd.play(datafD5, fD5)
        elif char == '3':
            sd.play(datafE5, fE5)
        elif char == '4':
            sd.play(datafF5, fF5)
        elif char == '5':
            sd.play(datafG5, fG5)
        elif char == '6':
            sd.play(datafA5, fA5)
        elif char == '7':
            sd.play(datafB5, fB5)
        elif char == '8':
            sd.play(datafC6, fC6)
        elif char == '9':
            sd.play(datafD6, fD6)

        elif char == '\x1b':
            sys.exit()

if __name__ == "__main__":
    test()
