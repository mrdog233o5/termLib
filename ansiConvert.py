class ansiConverter:
    def __init__(self):
        self.RESET = "\33[0m]"
        self.RESET = self.RESET.rstrip(self.RESET[-1])

    def ansiText(self, text, rgb=(255,255,255)):
        r,g,b = rgb
        ret = f"\033[38;2;{r};{g};{b}m{str(text)}]"
        return ret.rstrip(ret[-1])+self.RESET

    def ansiBlock(self, rgb=(255,255,255)):
        r,g,b = rgb
        ret = f"\033[48;2;{r};{g};{b}m ]"
        return ret.rstrip(ret[-1])+self.RESET
