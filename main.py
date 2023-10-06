import time

class terminator():
    def __init__(self, color=[-1,-1,-1]):
        self.color = color

    def cprint(self, text, color):
        print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{str(text)}\x1b[0m", end="")

    def aprint(self, message, WaitTime=0.02):
        for i in message:
            self.cprint(i, color=self.color)
            time.sleep(WaitTime)

    def printGrid(self, grid, space=10, revert=False):
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

a = [
    ["foo1", "bar1", "cao11123", "mum1324"],
    ["foo1asdf", "barqewr", "caoqw", "mumdh"],
    ["foosda", "barfs", "caosdas", "mumgfd"]
]
term = terminator(color=[100,100,100])
term.aprint("fuck my family")
