# MONOLITH OF INFORMATION
# Turns right on a black cell, turns left on a white cell and reverts the color before moving forward. 
# The simulation has wrapping walls so left and right edges are connected, same with top and bottom.
# Run this on terminal to see it in its full beauty. Use the interruption shortcut to stop it. (Probably Ctrl+C or Ctrl+D)
# Took some of the code from my Game of Life script as they both require similar things to run.

import time

size = 60 #Modify this number to experiment with different grid sizes. 
grid = [[0 for i in range(size)] for j in range(size)] #Generates a grid of cells with random states.
direction = 0 #0 is up, 1 is right, 2 is down, 3 is left.
x, y = size // 2, size // 2

def main():
    while True:
        print("\033[H\033[J", end="") #Allegedly, this somehow moves the cursor to the start of the terminal. Gemini gave me that, don't ask me. 💀
        nextGrid()
        print("\n".join("".join("█" if cur == 0 else " " for cur in row) for row in grid))
        time.sleep(0.005)
    return

def nextGrid():
    global x, y, direction
    if grid[x][y] == 0:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    grid[x][y] = 1 - grid[x][y]
    if direction == 0:
        x = (x - 1) % size
    elif direction == 1:
        y = (y + 1) % size
    elif direction == 2:
        x = (x + 1) % size
    else:
        y = (y - 1) % size
    return

main()