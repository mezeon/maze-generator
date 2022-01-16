from random import randint as r
from sys import argv
from PIL import Image

exit = False
blocks = set()

try: size = int(argv[1])
except: size = 75

try: offshoots = int(argv[2])
except: offshoots = 300

img = Image.new('1', (size + 2, size + 2))

img.putpixel((size // 2, 0), 1)
img.putpixel((size // 2, 1), 1)

# main line
last_step = [size // 2, 1]
for i in range(offshoots):
    last_step = (r(0, size - 1), r(0, size - 1))
    while img.getpixel(last_step) != 1:
        last_step = (r(0, size - 1), r(0, size - 1))
    while last_step[1] != size:
        # 0 - left, 1 - top, 2 - right, 3 - bottom
        # coordinates are starting from upper left corner
        direction = r(0, 3)

        if (direction == 0) and (img.getpixel((last_step[0] - 1, last_step[1] - 1)) == 0) and (img.getpixel((last_step[0] - 2, last_step[1] - 1)) == 0) and (img.getpixel((last_step[0] - 2, last_step[1])) == 0) and (img.getpixel((last_step[0] - 2, last_step[1] + 1)) == 0) and (img.getpixel((last_step[0] - 1, last_step[1] + 1)) == 0) and (last_step[0] - 1 > 0):
                last_step = (last_step[0] - 1, last_step[1])
                img.putpixel(last_step, 1)
                blocks = set()

        elif (direction == 1) and (img.getpixel((last_step[0] - 1, last_step[1] - 1)) == 0) and (img.getpixel((last_step[0] - 1, last_step[1] - 2)) == 0) and (img.getpixel((last_step[0], last_step[1] - 2)) == 0) and (img.getpixel((last_step[0] + 1, last_step[1] - 2)) == 0) and (img.getpixel((last_step[0] + 1, last_step[1] - 1)) == 0) and (last_step[1] - 1 > 0):
            last_step = (last_step[0], last_step[1] - 1)
            img.putpixel(last_step, 1)
            blocks = set()

        elif (direction == 2) and (img.getpixel((last_step[0] + 1, last_step[1] - 1)) == 0) and (img.getpixel((last_step[0] + 2, last_step[1] - 1)) == 0) and (img.getpixel((last_step[0] + 2, last_step[1])) == 0) and (img.getpixel((last_step[0] + 2, last_step[1] + 1)) == 0) and (img.getpixel((last_step[0] + 1, last_step[1] + 1)) == 0) and (last_step[0] + 1 < size - 1):
                last_step = (last_step[0] + 1, last_step[1])
                img.putpixel(last_step, 1)
                blocks = set()

        elif (direction == 3) and (img.getpixel((last_step[0] - 1, last_step[1] + 1)) == 0) and (img.getpixel((last_step[0] - 1, last_step[1] + 2)) == 0) and (img.getpixel((last_step[0], last_step[1] + 2)) == 0) and (img.getpixel((last_step[0] + 1, last_step[1] + 2)) == 0) and (img.getpixel((last_step[0] + 1, last_step[1] + 1)) == 0):
                last_step = (last_step[0], last_step[1] + 1)
                img.putpixel(last_step, 1)
                blocks = set()

        else:
            blocks.add(direction)
        
        if len(blocks) == 4:
            last_step = (r(0, size - 1), r(0, size - 1))
            while img.getpixel(last_step) != 1:
                last_step = (r(0, size - 1), r(0, size - 1))
    
img = img.crop((0, 0, size, size + 1))
for i in range(size):
    img.putpixel((i, size), 0)

exit_coordinates = (r(0, img.size[0] - 1), img.size[1] - 2)
while img.getpixel(exit_coordinates) != 1:
    exit_coordinates = (r(0, img.size[0] - 1), img.size[1] - 2)
img.putpixel((exit_coordinates[0], exit_coordinates[1] + 1), 1)

img.save('maze.png')
print('Maze saved as maze.png\a')