import time
import sys
import os
class printer():
    def __init__(self, color=[-1,-1,-1]):
        self.color = color
    def print(self, text):
        print(text, end="")
    def printls(self, text):
        print(text)
    def cprint(self, text, color):
        print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{str(text)}\x1b[0m", end="")
    def aprint(self, message, WaitTime=0.02, end="\n"):
        for i in message:
            self.cprint(i, color=self.color)
            time.sleep(WaitTime)
        print(end, end="")
    def printgrid(self, grid, space=10, revert=False):
        if revert:
            grid = list(zip(*grid[::-1]))
            for i in range(len(grid)):
                grid[i] = list(reversed(grid[i]))
        for row in grid:
            for element in row:
                self.cprint(element, color=self.color)
                for i in range(space - len(element)):
                    self.cprint(" ", color=self.color)
            print("")
    def cleanln(self):
        sys.stdout.write('\r\33[K')
        sys.stdout.flush()

    def clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')
