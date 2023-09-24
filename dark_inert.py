import pygame
import Player as Player
from SpriteSheets import SpriteSheet as SP

pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Darkness Inert")

#LOAD ALL THE IMAGES
main_bkg = pygame.image.load("assets/Backgrounds/bkg.jpg")
# print(main_bkg.get_width(), main_bkg.get_height())
main_bkg = pygame.transform.scale(main_bkg, (main_bkg.get_width() * .125, main_bkg.get_height() * .125))
main_bkg2 = pygame.transform.flip(main_bkg, True, False)

moon = pygame.image.load("assets/Backgrounds/moon.png")
moon = pygame.transform.scale(moon, (int(moon.get_width() * 2.25), int(moon.get_height() * 2.25)))

full_hearts = pygame.image.load("assets/Hearts/Full Hearts/hearts_sprite.png").convert_alpha()
#half hearts
half_hearts = pygame.image.load("assets/Hearts/Half Hearts/half_hearts_sprite.png").convert_alpha()
#empty hearts

#armor hearts
armor_hearts = pygame.image.load("assets/Hearts/Armor Hearts/full_hearts_sprite.png").convert_alpha()
#SET UP ANIMATION VARIABLES
fhs = SP(full_hearts)
hhs = SP(half_hearts)
ahs = SP(armor_hearts)

full_hearts_list = []
half_hearts_list = []
full_armor_list = []

last_update_fulls = pygame.time.get_ticks()
last_update_halves = pygame.time.get_ticks()
last_update_full_arm = pygame.time.get_ticks()

animation_cooldown_full_hearts = 250
animation_cooldown_half_hearts = 100
animation_cooldown_full_armor = 325

frame_fulls = 0
frame_halves = 0
frame_farm = 0

#CREATE THE ANIMATION LIST
for x in range(4):
    full_hearts_list.append(fhs.get_image(x, 128, 128, BLACK))
    half_hearts_list.append(hhs.get_image(x, 128, 128, BLACK))

for x in range(2):
    full_armor_list.append(ahs.get_image(x,128,128,BLACK))

moving_left = False
moving_right = False

run = True
while run:
    screen.blit(main_bkg, (0,0))
    screen.blit(main_bkg2, (512,0))
    screen.blit(main_bkg, (1024,0))
    screen.blit(moon, (350,0))

    current_time = pygame.time.get_ticks()
    if current_time - last_update_fulls >= animation_cooldown_full_hearts:
        frame_fulls += 1
        if frame_fulls == len(full_hearts_list):
            frame_fulls = 0
        last_update_fulls = current_time
    if current_time - last_update_halves >= animation_cooldown_half_hearts:
        frame_halves += 1
        if frame_halves == len(full_hearts_list):
            frame_halves = 0
        last_update_halves = current_time
    if current_time - last_update_full_arm >= animation_cooldown_full_armor:
        frame_farm += 1
        if frame_farm == len(full_armor_list):
            frame_farm = 0
        last_update_full_arm = current_time

    shift_coeff = -35
    shift_coeff_full_arm = -35
    for shift in range(4):
        screen.blit(full_hearts_list[frame_fulls],(shift_coeff,-40))
        screen.blit(half_hearts_list[frame_halves],(shift_coeff, 0))
        screen.blit(full_armor_list[frame_farm],(shift_coeff_full_arm, 50))
        shift_coeff += 40
        shift_coeff_full_arm += 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()
pygame.quit()