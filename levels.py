from objects import *
from settings import *

level1 = [
    "                                                                      ",
    "                                                                      ",
    "                                  o                                   ",
    "                        ---              -           --               ",
    "       4      1     O                                                 ",
    "      --    ---      ---    --                                        ",
    "   o                                               ---                ",
    "  ---     3     o                             0           o           ",
    "        ----      ---               o         ---                     ",
    "     o                         ---                                    ",
    "    ---                                   ---                         ",
    "                   o                                      ---         ",
    "                 ---                ----                 o          2 ",
    "---                         --                    --       --    -  - ",

]

level2 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "        ---      --   --                                              ",
    "                               --              --                     ",
    "     --      ---                                                    - ",
    "                         ---                --   -                    ",
    "---                              --                             ---   ",
    "                                          --                          ",
    "   --                                              ---     -          ",
    "                                     ---                              ",
    "-                                                         --          ",
]

level1_width = len(level1[0]) * 100
level1_height = len(level1) * 30
level2_width = len(level2[0]) * 100
level2_height = len(level2) * 30


level_objects = pygame.sprite.Group()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height) # прозорий прямокутник з'являється у координата (0,0), він і відіграє роль камери

    def apply(self, target):
        return target.rect.move(self.state.topleft) # цей метод буде робити всі об'єкти гри видимими для камери

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect) # оновлюємо положення камери, відносно певної рухомої цілі (гравця)


# налаштування розмірів та положення камери
def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + W / 2, -t + H / 2 # налаштовуємо положення камери, відносно гравця

    l = min(0, l)                    # Не виходимо за ліву межу
    l = max(-(camera.width - W), l)  # Не виходимо за праву межу
    t = max(-(camera.height - H), t) # Не виходимо за нижню межу
    t = min(0, t)                    # Не виходимо за верхню межу

    return pygame.Rect(l, t, w, h)


camera = Camera(camera_config, level1_width, level1_height)


def draw_level(level: list):
    global key, box, door
    x = y = 0
    for row in level:
        for symbol in row:
            if symbol == "-":
                platform = MapObject(x, y, 100, 30, platform_image)
                level_objects.add(platform)
                platforms.add(platform)
            if symbol == 'o':
                coin = MapObject(x, y, 30, 30, coin_image)
                level_objects.add(coins)
                coins.add(coin)
            if symbol == '1':
                rose = MapObject(x, y, 35, 35, rose_image)
                level_objects.add(rose)
            if symbol == '2':
                door = MapObject(x, y, 80, 80, door_image)
                level_objects.add(door)
            if symbol == '3':
                box = MapObject(x, y, 60, 60, box_image)
                level_objects.add(box)
            if symbol == '4':
                key = MapObject(x, y, 40, 40, key_image)
                level_objects.add(key)

            x +=100
        x = 0
        y += 50

    return level_objects, key, box, door, rose