"""solar - Solar system generative art

Usage:
  solar -w <width>  -s <sunsize> -v <height>
  solar (-h | --help)
  solar --version

Options:
  -w --width        Width of the image. Default: 3000
  -v --height       Height of the image. Default: 2000
  -s --sun-size     Set Sun size. Default: 300
  -b --border-size  Border thickness. Default: 50
  -n --noise        Grain. Default: 4
  -h --help         Show this screen.
  --version         Show the version.

"""

from docopt import docopt
import cairo
import PIL
import docopt
import math
import random
from PIL import Image, ImageDraw

version = '1.0'


def main():
    arg = docopt(__doc__, version=version)

    if arg['--guest-token']:
        print(get_guest_token())

def main():


if __name__ == '__main__':
    main()

