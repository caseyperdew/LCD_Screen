import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon
import time

BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x000000
FOREGROUND_COLOR = 0xC88428
WHITE = 0xFFFFFF
BLACK = 0x000000
RED = 0xFF0000
ORANGE = 0xFFA500
YELLOW = 0xFFFF00
TEXT_COLOR = 0xFFFF00
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3
dbus = displayio.FourWire(spi,command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus,rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
splash = displayio.Group()
display.root_group = splash
color_bitmap = displayio.Bitmap(display.width,display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader = color_palette, x=0, y=0)
splash.append(bg_sprite)

#tail feathers

#leftmost
blue = Triangle(120,65, 50, 15, 70, 15, fill = YELLOW , outline = YELLOW)
splash.append(blue)

orange = Triangle(120,65, 80, 10, 60, 10, fill = ORANGE , outline = ORANGE)
splash.append(orange)

yellow = Triangle(120,65, 70, 5, 90, 5, fill = YELLOW , outline = YELLOW)
splash.append(yellow)

red = Triangle(120,65, 100, 3, 80, 3, fill = ORANGE , outline = ORANGE)
splash.append(red)

#rightmost
teal = Triangle(120,65, 190, 15, 170, 15, fill = YELLOW , outline = YELLOW)
splash.append(teal)

gray = Triangle(120,65, 160, 10, 180, 10, fill = ORANGE , outline = ORANGE)
splash.append(gray)

black = Triangle(120,65, 170, 5, 150, 5, fill = YELLOW , outline = YELLOW)
splash.append(black)

white = Triangle(120,65, 130, 3, 160, 3, fill = ORANGE , outline = ORANGE)
splash.append(white)

#middle
violet = Triangle(120,65, 150, 2, 90, 2, fill = YELLOW , outline = YELLOW)
splash.append(violet)

purple = Triangle(120,65, 100, 2, 140, 2, fill = ORANGE , outline = ORANGE)
splash.append(purple)

lilac = Triangle(120,65, 110, 2, 130, 2, fill = YELLOW , outline = YELLOW)
splash.append(lilac)

seafoam = Triangle(120,65, 115, 2, 125, 2, fill = ORANGE , outline = ORANGE)
splash.append(seafoam)


#Body
lightBlue = Circle(120, 67, 40, fill = FOREGROUND_COLOR, outline = FOREGROUND_COLOR, stroke = 2)
splash.append(lightBlue)

#beak
forest = Triangle(120,75, 120, 65, 130, 70, fill = YELLOW , outline = YELLOW)
splash.append(forest)

#left eye
dark = Circle(100, 50, 7, fill = WHITE, outline = WHITE, stroke = 2)
splash.append(dark)

#right eye
light = Circle(140, 50, 7, fill = WHITE, outline = WHITE, stroke = 2)
splash.append(light)

#left pupil
redOrange = Circle(101, 50, 3, fill = BLACK, outline = BLACK, stroke = 2)
splash.append(redOrange)

#right pupil
pink = Circle(141, 50, 3, fill = BLACK, outline = BLACK, stroke = 2)
splash.append(pink)

#red thingy
green = RoundRect(110, 65, 10, 30,5, fill = RED, outline = RED, stroke = 2)
splash.append(green)

#brown triangle for movement
brown = Triangle(130,70, 140, 65, 140, 75, fill = FOREGROUND_COLOR , outline = FOREGROUND_COLOR)
splash.append(brown)

direction_x = 1
velocity_x = 1


direction_x2 = 1
velocity_x2 = 1

direction_x3 = 1
velocity_x3 = 2

while True:
    if redOrange.x >= 104 or redOrange.x <= 97:
        direction_x *= -1
    redOrange.x += (velocity_x * direction_x)

    
    if pink.x >= 144 or pink.x <= 137:
        direction_x2 *= -1
    pink.x += (velocity_x2 * direction_x2)

    if brown.x >= 140 or brown.x <= 123:
        direction_x3 *= -1
    brown.x += (velocity_x3 * direction_x3)
    
    time.sleep(.15)
    

