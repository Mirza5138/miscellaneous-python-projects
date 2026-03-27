# MONOLITH OF INFORMATION
# █ is alive, " " is dead. The simulation has wrapping walls so left and right edges are connected, same with top and bottom.
# Run this on terminal to see it in its full beauty. Use the interruption shortcut to stop it. (Probably Ctrl+C or Ctrl+D)
# Even though i wrote most of the lines, i unfortunately had to get help from Gemini to fix and optimize a few things.

from random import *
import time

size = 150 #Modify this number to experiment with different grid sizes. Bigger grids usually takes longer to stabilize.
grid = [[randint(0,1) for i in range(size)] for j in range(size)] #Generates a grid of cells with random states.
new_grid = [[0 for i in range(size)] for j in range(size)]

def main():
    while True:
        print("\033[H\033[J", end="") #Allegedly, this somehow moves the cursor to the start of the terminal. Idk why, Gemini didn't tell me.
        nextGrid()
        print("\n".join("".join("█" if cur == 1 else " " for cur in row) for row in grid))
        time.sleep(0.04)
    return

def nextGrid():
    global grid
    for i in range(size):
        for j in range(size):
            nbSum = neighbourSum(grid, i, j)
            current = grid[i][j]

            if nbSum == 3:
                new_grid[i][j] = 1
            elif nbSum == 2:
                new_grid[i][j] = current
            else:
                new_grid[i][j] = 0

    grid = [list(i) for i in new_grid]

def neighbourSum(the_grid, x, y):
    sum = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue

            nx = (x + dx) % size
            ny = (y + dy) % size
            
            sum += the_grid[nx][ny]
            
    return sum

main()
