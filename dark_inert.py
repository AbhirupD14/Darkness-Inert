import pygame
import Player as Player
from SpriteSheets import SpriteSheet as SP
pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Darkness Inert")

BLACK = (0,0,0)

main_bkg = pygame.image.load("assets/Backgrounds/bkg.jpg")
# print(main_bkg.get_width(), main_bkg.get_height())
main_bkg = pygame.transform.scale(main_bkg, (main_bkg.get_width() * .125, main_bkg.get_height() * .125))
main_bkg2 = pygame.transform.flip(main_bkg, True, False)

moon = pygame.image.load("assets/Backgrounds/moon.png")
moon = pygame.transform.scale(moon, (int(moon.get_width() * 2.25), int(moon.get_height() * 2.25)))

full_hearts = pygame.image.load("assets/Hearts/hearts_sprite.png").convert_alpha()
fhs = SP(full_hearts)

full_hearts_list = []
half_hearts_list = []
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown_full_hearts = 250
animation_cooldown_half_hearts = 100
frame = 0

for x in range(animation_steps):
    full_hearts_list.append(fhs.get_image(x, 128, 128, BLACK))

moving_left = False
moving_right = False

run = True
while run:
    screen.blit(main_bkg, (0,0))
    screen.blit(main_bkg2, (512,0))
    screen.blit(main_bkg, (1024,0))
    screen.blit(moon, (350,0))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown_full_hearts:
        frame += 1
        if frame == len(full_hearts_list):
            frame = 0
        last_update = current_time
    shift_coeff = -35
    for shift in range(4):
        screen.blit(full_hearts_list[frame],(shift_coeff,-40))
        shift_coeff += 40

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()
pygame.quit()