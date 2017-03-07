#!/usr/bin/python

# https://github.com/pimoroni/blinkt/tree/master/examples

from __future__ import print_function
from blinkt import set_all, set_clear_on_exit, set_pixel, show, set_brightness
import time
import sys


set_clear_on_exit()

# set_pixel(0,255,0,0)
# show()

# COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 153, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# constants used in the app to display status
CHECKING_COLOR = BLUE
SUCCESS_COLOR = GREEN
FAILURE_COLOR = RED


def all_off():
    set_all(0, 0, 0)
    show()


def all_on(color):
    set_all(color[0], color[1], color[2])


def flash_up(color, delay):
    all_off()
    time.sleep(delay)
    for y in range(8):
        set_pixel(y, color[0], color[1], color[2])
        show()
        time.sleep(delay)


def flash_all(flash_count, delay, color):
    # light all of the LEDs in a RGB single color. Repeat 'flash_count' times
    # keep illuminated for 'delay' value
    for index in range(flash_count):
        all_on(color)
        time.sleep(delay)
        all_off()
        time.sleep(delay)


def main():
    while 1:
        flash_up(ORANGE, .10)
        # wait a second then check again
        # You can always increase the sleep value below to check less often
        time.sleep(1)

    # this should never happen since the above is an infinite loop
    print('Leaving main()')


# Now see what we're supposed to do next
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting application\n')
        sys.exit(0)
