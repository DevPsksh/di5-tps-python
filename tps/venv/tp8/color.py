class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_luminance(self):
        return 0.2426 * self.r + 0.715 * self.g + 0.0722 * self.b

    def clone_from(self, color):
        self.r = color.r
        self.g = color.g
        self.b = color.b

    def clone(self):
        return Color(self.r, self.g, self.b)

