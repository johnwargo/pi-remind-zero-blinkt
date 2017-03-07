#!/usr/bin/python

# https://github.com/pimoroni/blinkt/tree/master/examples

from __future__ import print_function

import sys
import time

from blinkt import set_all, set_clear_on_exit, set_pixel, show

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
BLACK = (0, 0, 0)


def all_off():
    set_all(0, 0, 0)
    show()


def all_on(color):
    set_all(color[0], color[1], color[2])
    show()


def flash_up(color, delay):
    time.sleep(delay)
    for y in range(8):
        set_pixel(y, color[0], color[1], color[2])
        show()
        time.sleep(delay)


def flash_down(color, delay):
    for y in range(8):
        set_pixel(7 - y, color[0], color[1], color[2])
        show()
        time.sleep(delay)


def zip_zip(color, delay):
    for y in range(4):
        set_pixel(y, color[0], color[1], color[2])
        set_pixel(7 - y, color[0], color[1], color[2])
        show()
        time.sleep(delay)
    for y in range(4):
        set_pixel(y, BLACK[0], BLACK[1], BLACK[2])
        set_pixel(7 - y, BLACK[0], BLACK[1], BLACK[2])
        show()
        time.sleep(delay)


def up_down(color, delay):
    for y in range(8):
        set_pixel(7 - y, color[0], color[1], color[2])
        show()
        time.sleep(delay)
    for y in range(8):
        set_pixel(y, BLACK[0], BLACK[1], BLACK[2])
        show()
        time.sleep(delay)


def flash(flash_count, delay, color):
    # light all of the LEDs in a RGB single color. Repeat 'flash_count' times
    # keep illuminated for 'delay' value
    for index in range(flash_count):
        all_on(color)
        time.sleep(delay)
        all_off()
        time.sleep(delay)


def main():
    all_off()
    while 1:
        # flash_down(ORANGE, .10)
        # flash_up(BLACK, .10)
        # up_down(ORANGE, .10)
        zip_zip(ORANGE, .10)
        flash(3, .25, RED)
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
