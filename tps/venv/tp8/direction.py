LEFT = 0
BOTTOM = 1
RIGHT = 2
TOP = 3


def left(direction):
    if direction < 0 or direction > 3:
        raise Exception()
    res = direction + 1
    if res > 3:
        return 0
    else:
        return res


def right(direction):
    if direction < 0 or direction > 3:
        raise Exception()
    res = direction - 1
    if res < 0:
        return 3
    else:
        return res


def to_xy(direction):
    if direction == LEFT:
        return -1, 0
    elif direction == BOTTOM:
        return 0, -1
    elif direction == RIGHT:
        return 1, 0
    elif direction == TOP:
        return 0, 1
    else:
        raise Exception()

