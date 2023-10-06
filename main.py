import time
import sys
import os

class ansiConverter:
    def __init__(self):
        self.RESET = "\33[0m]"
        self.RESET = self.RESET.rstrip(self.RESET[-1])

    def rgb_ansi(self, text, rgb=[255,255,255]):
        r,g,b = rgb[0],rgb[1],rgb[2]
        ret = f"\033[38;2;{r};{g};{b}m{str(text)}]"
        return ret.rstrip(ret[-1])

class printer:
    def __init__(self, color=[-1,-1,-1]):
        self.color = color

    def cprint(self, msg, color):
        tempClass = ansiConverter()
        print(tempClass.rgb_ansi(msg, rgb=color), end="")

    def aprint(self, message, WaitTime=0.015, end="\n"):
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
        temp = '\r\33[K]'
        sys.stdout.write(temp.strip(temp[-1]))
        sys.stdout.flush()

    def clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')

a = printer((17, 196, 17))
a.aprint("asdkfuhqweoaidskljfhoiqukljehasdflkujhqwef2891ui3oweqd")
