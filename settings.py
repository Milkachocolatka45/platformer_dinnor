import pygame

pygame.init()

W, H = 1280, 700
FPS = 20
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Money PEOPLE")
pygame.display.set_icon(pygame.image.load('assets/images/player/stand_1.png'))

clock = pygame.time.Clock()

platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()
bg = pygame.transform.scale(pygame.image.load("assets/images/1626767904_11-kartinkin-com-p-galakticheskii-fon-krasivo-22.jpg"), (W, H))

platform_image = pygame.image.load("assets/images/98914879c7817315d7734f9930f5abc0.webp")


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