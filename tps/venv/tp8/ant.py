import color
import direction as _direction


def from_json(json, x, y, direction):
    return Ant(
        x, y, direction, json["size"],
        color.Color(json["color_red"], json["color_green"], json["color_blue"]),
        color.Color(json["follow_color_red"], json["follow_color_green"], json["follow_color_blue"]),
        json["left_proba"],
        json["right_proba"],
        json["follow_proba"],
        json["move_type"]
    )


CONVOLUTION_MATRIX3 = [
    [1 / 4, 2 / 4, 1 / 4],
    [2 / 4, 4 / 4, 2 / 4],
    [1 / 4, 2 / 4, 1 / 4]
]
CONVOLUTION_MATRIX5 = [
    [1 / 14, 2 / 14, 3 / 14, 2 / 14, 1 / 14],
    [2 / 14, 4 / 14, 7 / 14, 4 / 14, 2 / 14],
    [3 / 14, 7 / 14, 14 / 14, 7 / 14, 3 / 14],
    [2 / 14, 4 / 14, 7 / 14, 4 / 14, 2 / 14],
    [1 / 14, 2 / 14, 3 / 14, 2 / 14, 1 / 14]
]


class Ant:

    def __init__(self, x, y, direction, size, color, follow_color, left_proba, right_proba, follow_proba, move_type):
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size
        self.color = color
        self.follow_color = follow_color
        self.left_proba = left_proba
        self.right_proba = right_proba
        self.follow_proba = follow_proba
        self.move_type = move_type

    def move(self, direction):
        (x, y) = _direction.to_xy(direction)
        self.x += x
        self.y += y
        self.direction = direction

    def should_follow(self, color):
        tmp = abs(self.follow_color.get_luminance() - color.get_luminance())
        return tmp < 40

