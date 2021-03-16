"""solar - Solar system generative art

Usage:
  solar [ -w <width>  -s <sunsize> -v <height> -b <bordersize> -n <noise> ]
  solar (-h | --help)
  solar --version

Options:
  -w --width <width>             Width of the image [default: 3000].
  -v --height <height>           Height of the image [default: 2000].
  -s --sun-size <sunsize>        Set Sun size [default: 300].
  -b --border-size <bordersize>  Border thickness [default: 50].
  -n --noise <noise>             Grain [default: 4].
  -h --help                      Show this screen.
  --version                      Show the version.

"""

from PIL import Image, ImageDraw
from docopt import docopt
import PIL
import cairo
import docopt
import math
import random

list_of_colors = [
    ( 29,  32,  33), ( 40,  40,  40), ( 50,  48,  47), ( 60,  56,  54),
    ( 80,  73,  69), (102,  92,  84), (124, 111, 100), (146, 131, 116),
    (146, 131, 116), (249, 245, 215), (251, 241, 199), (242, 229, 188),
    (235, 219, 178), (213, 196, 161), (189, 174, 147), (168, 153, 132),
    (251,  73,  52), (184, 187,  38), (250, 189,  47), (131, 165, 152),
    (211, 134, 155), (142, 192, 124), (254, 128,  25), (204,  36,  29),
    (152, 151,  26), (215, 153,  33), ( 69, 133, 136), (177,  98, 134),
    (104, 157, 106), (214,  93,  14), (157,   0,   6), (121, 116,  14),
    (181, 118,  20), (  7, 102, 120), (143,  63, 113), ( 66, 123,  88),
    (175,  58,   3),
]


version = '1.0'


def draw_background(cr, r, g, b, width, height):
    cr.set_source_rgb(r, g, b)
    cr.rectangle(0, 0, width, height)
    cr.fill()


def main():
    arg = docopt.docopt(__doc__, version=version)

    print(arg)

    width       = arg['--width']
    height      = arg['--height']
    border_size = arg['--bordersize']
    sun_size    = arg['--sunsize']
    sun_center  = height - border_size

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)

    draw_background(cr, .3, .3, .3, width, height)

    sun_color = random.choice(list_of_colors)


if __name__ == '__main__':
    main()

