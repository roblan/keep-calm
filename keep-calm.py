import sys
import argparse
from os import path
from PIL import Image, ImageFont, ImageDraw
from inky import InkyWHAT

parser = argparse.ArgumentParser()
parser.add_argument('--colour', '-c', type=str, required=True, choices=["red", "black", "yellow"], help="ePaper display colour")
parser.add_argument('--text', '-t', type=str, nargs=5, help="keep calm message", default=["keep", "calm", "and", "carry", "on"])
args = parser.parse_args()

BACKGROUND = args.colour
inky_display = InkyWHAT(BACKGROUND)
inky_display.set_border(inky_display.WHITE)
WIDTH = inky_display.WIDTH
HEIGHT = inky_display.HEIGHT
MARGIN = 20
LINES = args.text
TEXT = "white"
FONTSIZE = 30
DIRNAME = path.dirname(__file__)

img = Image.new("P", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)
draw.rectangle([(0,0), img.size], BACKGROUND)

fontsize = FONTSIZE
lines = map(str.upper, LINES)
def getFont(line, size, index = 0):
    font = ImageFont.truetype(path.join(DIRNAME, "font.ttf"), size if index != 2 else int(2 * round(size / 4)))
    width, height = font.getsize(line)
    return (width, height, font)

maxlength = 0
while True:
    for n, line in enumerate(lines):
        width, height, font = getFont(line, fontsize, n)
        maxlength = max(width, maxlength)
    if maxlength < WIDTH - (2 * MARGIN):
        break
    else:
        maxlength = 0
        fontsize = fontsize - 1

# if fontsize smaller than default - calculate, else - take margin
y = HEIGHT - (MARGIN if fontsize == FONTSIZE else ((WIDTH - maxlength) / 2)) + fontsize / 2;

for n, line in enumerate(reversed(lines)):
    width, height, font = getFont(line, fontsize, n)
    x = (WIDTH / 2) - (width / 2)
    y = y - height - (fontsize / 2);
    draw.text((x, y), line, TEXT, font)

crown = "^"
width, height, font = getFont(crown, 77)
x = (WIDTH / 2) - (width / 2)
y = (y / 2) - (height / 2) - 5
draw.text((x, y), crown, TEXT, font)

pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
img = img.convert("RGB").quantize(palette=pal_img)

inky_display.set_image(img)
inky_display.show()
