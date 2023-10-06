import time

def rgbToAnsi(r, g, b):
    if r == g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232

    ansi_r = 36 * round(r / 255 * 5)
    ansi_g = 6 * round(g / 255 * 5)
    ansi_b = round(b / 255 * 5)

    return 16 + ansi_r + ansi_g + ansi_b

class terminator():
    def __init__(self, color=[-1,-1,-1]):
        self.color = rgbToAnsi(color[0], color[1], color[2])
    def cprint(self, text, color=16):
        if color == 16:
            print(text, end="")
            return
        print(f"\033[38;5;{color}m{text}\033[0m")
    def cprintln(self):
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
            self.cprint(" ", color=self.color)

a = [
    ["foo1", "bar1", "cao11123", "mum1324"],
    ["foo1asdf", "barqewr", "caoqw", "mumdh"],
    ["foosda", "barfs", "caosdas", "mumgfd"]
]
term = terminator()
term.printGrid(a, space=20, revert=True)
