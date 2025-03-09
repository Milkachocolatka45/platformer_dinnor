import pygame

pygame.init()

W, H = 1280, 700
FPS = 20
coins_count = 0
is_key = False

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Money PEOPLE")
pygame.display.set_icon(pygame.image.load('assets/images/player/stand_1.png'))

clock = pygame.time.Clock()
#ГРУПИ СПРАЙТІВ
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()
#КАРТИНКИ СПРАЙТІВ
bg = pygame.transform.scale(pygame.image.load("assets/background/1611928591_30-p-zadnii-fon-dlya-igri-31.jpg"), (W, H))

platform_image = pygame.image.load("assets/background/883423440-3880-akvariumnij-zadnij-fon-aqua-nova-sinij-chornij-60x30sm-black-blue-s_sn-560x420.jpg")


player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png"),
]

coin_image  = pygame.image.load("assets/images/coin/coin_icon.png")
door_image = pygame.image.load("assets/door/images__1_-removebg-preview.png")
rose_image = pygame.image.load("assets/rose/images-removebg-preview.png")
box_image = pygame.image.load("assets/box/4230567.png")
key_image = pygame.image.load("assets/key/png-transparent-graphy-metal-key-text-photography-metal-background-thumbnail-removebg-preview.png")

#ШРИФТИ
pygame.font.init()
font1 = pygame.font.Font(None, 50)