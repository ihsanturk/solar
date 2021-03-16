"""solar - Solar system generative art

Usage:
  solar [ options ]
  solar (-h | --help)
  solar --version

Options:
  -w --width <width>             Width of the image [default: 2560].
  -v --height <height>           Height of the image [default: 1600].
  -o --orbit                     Use orbits.
  -l --line                      Use linear lines.
  -g --gaps                      Use gaps.
  -s --sun-size <sunsize>        Set Sun size.
  -b --border-size <bordersize>  Border thickness [default: 5].
  -n --noise <noise>             Grain.
  -p --preset <preset>           "13inch-retina", "iphone-se", "iphone-x", ...
  -h --help                      Show this screen.
  --version                      Show the version.

"""

from PIL import Image, ImageDraw
from docopt import docopt
import PIL
import cairo
import math
import random

colors = [
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


float_gen = lambda a, b: random.uniform(a, b)


def draw_border(cr, size, r, g, b, width, height, use_gaps=False):
    # TODO: make gaps size adjustable
    if use_gaps:
        gaps = max(width, height) * 0.01
    else:
        gaps = 0
    cr.set_source_rgb(r, g, b)
    cr.rectangle(gaps, gaps, size, height - gaps)
    cr.rectangle(gaps, gaps, width - gaps, size + gaps)
    cr.rectangle(gaps, (height - gaps - size), width - gaps, size)
    cr.rectangle(width-size, 0, size, height)
    cr.fill()


def draw_orbit(cr, line, x, y, radius, r, g, b):
    cr.set_line_width(line)
    cr.arc(x, y, radius, 0, 2*math.pi)
    cr.stroke()


def draw_circle_fill(cr, x, y, radius, r, g, b):
    cr.set_source_rgb(r, g, b)
    cr.arc(x, y, radius, 0, 2*math.pi)
    cr.fill()


def draw_background(cr, r, g, b, width, height):
    cr.set_source_rgb(r, g, b)
    cr.rectangle(0, 0, width, height)
    cr.fill()


def main():
    arg = docopt(__doc__, version=version)

    resolution_presets = {
        "15inch-retina": (3072, 1920),
        "13inch-retina": (2560, 1600),
        "iphone-5s":     (750,  1334),
        "iphone-se":     (750,  1334),
    }

    width       = int(arg['--width'])
    height      = int(arg['--height'])
    border_size = float(arg['--border-size'])
    sun_size    = max(width, height)/10 if not arg['--sun-size'] else float(arg['--sun-size'])
    sun_center  = height - border_size
    arg_noise = max(width,height)/10000 if not arg['--noise'] else float(arg['--noise'])

    if arg['--preset'] is not None:
        if arg['--preset'] in resolution_presets:
            width, height = arg['--preset']
        else:
            print('available presets are:')
            for p in resolution_presets:
                print(f'\t{p}')

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)

    draw_background(cr, .2, .2, .2, width, height)

    sun_color = random.choice(colors)
    sun_r = sun_color[0]/255.0
    sun_g = sun_color[1]/255.0
    sun_b = sun_color[2]/255.0

    draw_circle_fill(cr, width/2, sun_center, sun_size, sun_r, sun_g, sun_b)

    distance_between_planets = 20
    last_center = sun_center
    last_size = sun_size
    last_color = sun_color

    min_size = 5
    max_size = 70

    for x in range(1, 20):
        next_size = random.randint(min_size, max_size)
        next_center = last_center - last_size - (next_size * 2) - distance_between_planets

        if not(next_center - next_size < border_size):
            if arg['--orbit']:
                draw_orbit(cr, 4, width/2, sun_center,
                        height - next_center - border_size,
                        .6, .6, .6)
            elif(arg['--line']):
                cr.move_to(border_size * 2, next_center)
                cr.line_to(width-(border_size*2), next_center)
                cr.stroke()

            draw_circle_fill(cr, width/2, next_center, next_size*1.3, .2, .2, .2)

            random_color = random.choice(colors)
            while(random_color is last_color):
                random_color = random.choice(colors)

            last_color = random_color

            r, g, b = random_color[0]/255.0, random_color[1]/255.0, random_color[2]/255.0
            draw_circle_fill(cr, width/2, next_center, next_size, r, g, b)

            last_center = next_center
            last_size = next_size

            min_size += 5
            max_size += 5 * x

    draw_border(cr, border_size, sun_r, sun_g, sun_b, width, height,
                use_gaps=arg['--gaps'])

    ims.write_to_png('solar.png')

    # noise
    pil_image = Image.open('solar.png')
    pixels = pil_image.load()
    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            r, g, b = pixels[i, j]
            noise = float_gen(1.0 - arg_noise, 1.0 + arg_noise)
            pixels[i, j] = (int(r * noise), int(g * noise), int(b * noise))
    pil_image.save('solar-noise.png')

if __name__ == '__main__':
    main()

