import random
import matplotlib.pyplot as plt
import ant as _ant
import color
import config
import direction

CONFIG = config.load()
WORLD_WIDTH = CONFIG["world_width"]
WORLD_HEIGHT = CONFIG["world_height"]
ITERATIONS_COUNT = CONFIG["iterations_count"]

WORLD = [[[0.0 for x in range(3)] for y in range(WORLD_HEIGHT)] for z in range(WORLD_WIDTH)]
ANTS = [_ant.from_json(it, random.randint(0, WORLD_WIDTH), random.randint(0, WORLD_HEIGHT), direction.BOTTOM) for it in
        CONFIG["ants"]]

# print(WORLD, len(WORLD), len(WORLD[0]), len(WORLD[0][0]))


def is_in_world(x, y):
    return 0 <= x < WORLD_WIDTH and 0 <= y < WORLD_HEIGHT


def get_world_color(x, y):
    tmp = WORLD[x][y]
    return color.Color(tmp[0], tmp[1], tmp[2])


def move_ant_follow(ant, dir):
    dx, dy = direction.to_xy(dir)
    x, y = ant.x + dx, ant.y + dy
    if is_in_world(x, y) and ant.should_follow(get_world_color(x, y)):
        ant.move(dir)
        return True
    else:
        return False


def move_ant(ant):
    if random.random() < ant.follow_proba:
        if move_ant_follow(ant, ant.direction): return
        if move_ant_follow(ant, direction.left(ant.direction)): return
        if move_ant_follow(ant, direction.right(ant.direction)): return

    rand = random.random()

    if rand < ant.right_proba:
        ant.move(direction.right(ant.direction))
    elif rand < ant.right_proba + ant.left_proba:
        ant.move(direction.left(ant.direction))
    else:
        ant.move(ant.direction)

    if ant.x < 0:
        ant.x = 0
    elif ant.x >= WORLD_WIDTH:
        ant.x = WORLD_WIDTH - 1

    if ant.y < 0:
        ant.y = 0
    elif ant.y >= WORLD_HEIGHT:
        ant.y = WORLD_HEIGHT - 1


def draw_ant(ant):
    if ant.size == 1:
        WORLD[ant.x][ant.y][0] = ant.color.r
        WORLD[ant.x][ant.y][1] = ant.color.g
        WORLD[ant.x][ant.y][2] = ant.color.b
    elif ant.size == 2:
        for i in range(0, 3):
            for j in range(0, 3):
                x, y = ant.x + i - 2, ant.y + j - 2
                if is_in_world(x, y):
                    conv = _ant.CONVOLUTION_MATRIX3[i][j]
                    WORLD[x][y][0] = ant.color.r * conv + WORLD[x][y][0] * (1 - conv)
                    WORLD[x][y][1] = ant.color.g * conv + WORLD[x][y][1] * (1 - conv)
                    WORLD[x][y][2] = ant.color.b * conv + WORLD[x][y][2] * (1 - conv)
    elif ant.size == 3:
        for i in range(0, 5):
            for j in range(0, 5):
                x, y = ant.x + i, ant.y + j
                if is_in_world(x, y):
                    conv = _ant.CONVOLUTION_MATRIX5[i][j]
                    WORLD[x][y][0] = ant.color.r * conv + WORLD[x][y][0] * (1 - conv)
                    WORLD[x][y][1] = ant.color.g * conv + WORLD[x][y][1] * (1 - conv)
                    WORLD[x][y][2] = ant.color.b * conv + WORLD[x][y][2] * (1 - conv)
    else:
        raise Exception()


# MAIN

# plt.ion()
plt.imshow(WORLD)
plt.show()

for i in range(ITERATIONS_COUNT):
    for ant in ANTS:
        move_ant(ant)
        draw_ant(ant)
    # IMAGE.set_data(WORLD)
    # IMAGE.set_array(WORLD)
    # plt.draw()
    plt.imshow(WORLD)
    plt.show()
    # time.sleep(1)

#--------------------La partie (Thread)--------------------------#

#from afficheur import Afficheur

# Create threads
#thread1 = Afficheur("1")
#thread2 = Afficheur("2")

#thread1.start()
#thread2.start()

#thread1.join()
#thread2.join()

