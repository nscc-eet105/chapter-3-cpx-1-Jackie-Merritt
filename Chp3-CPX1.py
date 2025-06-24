#Jackie_Merritt-Chp3_CPXLab1-6/24/2025
from adafruit_circuitplayground import cp
import time

#Switch
while True:
    if cp.switch:
        cp.red_led = True
        cp.play_file("blip.wav")
    else:
        cp.red_led = False

#Button

    if cp.button_a:
        cp.red_led = True
        cp.play_file("applause_y.wav")
    else:
        cp.red_led = False

    if cp.button_b:
        cp.red_led = True
        cp.play_file("bloop_x.wav")
    else:
        cp.red_led = False

#Touch

    if cp.touch_A1:
        cp.pixels[0] = (0, 100, 100) #
    else:
        cp.pixels[0] = (0, 0, 0) #all off
