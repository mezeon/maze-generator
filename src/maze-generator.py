from random import randint as r
from sys import argv
from PIL import Image
from time import time

start = time()
blocks = set()

# size of the maze - output image will have size (size, size)
try: size = int(argv[1])
except: size = 100

# level of offshoots
try: offshoots = int(argv[2])
except: offshoots = 100

maze = []
for w in range(size + 2):
    maze.append([])
    for h in range(size + 2):
        maze[w].append(0)

maze[size // 2][0] = 1
maze[size // 2][1] = 1

last_step = [size // 2, 1]
for i in range(offshoots):
    last_step = (r(0, size - 1), r(0, size - 1))
    while maze[last_step[0]][last_step[1]] != 1:
        last_step = (r(0, size - 1), r(0, size - 1))
    while last_step[1] != size - 2:
        # 0 - left, 1 - top, 2 - right, 3 - bottom
        # coordinates are starting from the upper left corner
        direction = r(0, 3)
    
        if (direction == 0) and (maze[last_step[0] - 1][last_step[1] - 1] == 0) and (maze[last_step[0] - 2][last_step[1] - 1] == 0) and (maze[last_step[0] - 2][last_step[1]] == 0) and (maze[last_step[0] - 2][last_step[1] + 1] == 0) and (maze[last_step[0] - 1][last_step[1] + 1] == 0) and (last_step[0] - 1 > 0):
            last_step = (last_step[0] - 1, last_step[1])
            maze[last_step[0]][last_step[1]] = 1
            blocks = set()

        elif (direction == 1) and (maze[last_step[0] - 1][last_step[1] - 1] == 0) and (maze[last_step[0] - 1][last_step[1] - 2] == 0) and (maze[last_step[0]][last_step[1] - 2] == 0) and (maze[last_step[0] + 1][last_step[1] - 2] == 0) and (maze[last_step[0] + 1][last_step[1] - 1] == 0) and (last_step[1] - 1 > 0):
            last_step = (last_step[0], last_step[1] - 1)
            maze[last_step[0]][last_step[1]] = 1
            blocks = set()

        elif (direction == 2) and (maze[last_step[0] + 1][last_step[1] - 1] == 0) and (maze[last_step[0] + 2][last_step[1] - 1] == 0) and (maze[last_step[0] + 2][last_step[1]] == 0) and (maze[last_step[0] + 2][last_step[1] + 1] == 0) and (maze[last_step[0] + 1][last_step[1] + 1] == 0) and (last_step[0] + 1 < size - 1):
            last_step = (last_step[0] + 1, last_step[1])
            maze[last_step[0]][last_step[1]] = 1
            blocks = set()

        elif (direction == 3) and (maze[last_step[0] - 1][last_step[1] + 1] == 0) and (maze[last_step[0] - 1][last_step[1] + 2] == 0) and (maze[last_step[0]][last_step[1] + 2] == 0) and (maze[last_step[0] + 1][last_step[1] + 2] == 0) and (maze[last_step[0] + 1][last_step[1] + 1] == 0) and (last_step[1] + 1 < size - 1):
            last_step = (last_step[0], last_step[1] + 1)
            maze[last_step[0]][last_step[1]] = 1
            blocks = set()

        else:
            blocks.add(direction)
        
        if len(blocks) == 4:
            last_step = (r(0, size - 1), r(0, size - 1))
            while maze[last_step[0]][last_step[1]] != 1:
                last_step = (r(0, size - 1), r(0, size - 1))

exit_coordinates = (r(0, size - 1), size - 2)
while maze[exit_coordinates[0]][exit_coordinates[1]] != 1:
    exit_coordinates = (r(0, size - 1), size - 2)
maze[exit_coordinates[0]][exit_coordinates[1] + 1] = 1

img = Image.new('1', (size, size))
for w in range(size):
    for h in range(size):
        img.putpixel((w, h), maze[w][h])

img.save('maze.png')
print('Maze saved as maze.png\a')
print('Generation took', round(time() - start, 3), 's')