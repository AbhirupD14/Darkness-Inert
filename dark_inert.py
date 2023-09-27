import pygame
from SpriteSheets import SpriteSheet as SP
#350 PIXELS IS THE GROUND
#hello
pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT  = 640
BLACK = (0,0,0)

monitor_rez = pygame.display.Info()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Darkness Inert")

#LOAD ALL THE IMAGES
main_bkg = pygame.image.load("assets/Backgrounds/bkg2.jpg")
print(main_bkg.get_width(), main_bkg.get_height())
main_bkg = pygame.transform.scale(main_bkg, (main_bkg.get_width() * .25, main_bkg.get_height() * .25))
main_bkg2 = pygame.transform.flip(main_bkg, True, False)

stick_fucker = pygame.image.load("assets/Backgrounds/unnamed.jpg")
# stick_fucker = pygame.transform.scale(stick_fucker, (stick_fucker.get_width() * .5, stick_fucker.get_height() * .5))
moon = pygame.image.load("assets/Backgrounds/moon.png")
moon = pygame.transform.scale(moon, (int(moon.get_width() * 2.25), int(moon.get_height() * 2.25)))

full_hearts = pygame.image.load("assets/Hearts/Full Hearts/hearts_sprite.png").convert_alpha()
half_hearts = pygame.image.load("assets/Hearts/Half Hearts/half_hearts_sprite.png").convert_alpha()
armor_hearts = pygame.image.load("assets/Hearts/Armor Hearts/full_hearts_sprite.png").convert_alpha()
empty_heart = pygame.image.load("assets/Hearts/Empty Hearts/empty_heart.png").convert_alpha()
empty_armor = pygame.image.load("assets/Hearts/Empty Hearts/armor_dead.jpg").convert_alpha()

#SET UP ANIMATION VARIABLES
fhs = SP(full_hearts)
hhs = SP(half_hearts)
ahs = SP(armor_hearts)

def make_animation_list(sprite_sht, animation_steps):
    animation_list = []
    for x in range(int(animation_steps)):
        animation_list.append(sprite_sht.get_image(x, 128, 128, BLACK))
    return animation_list

def animation_update(last_update, cur_time, animation_cooldown, h_list):
    frame = 0
    if cur_time - last_update >= animation_cooldown:
        frame += 1
        if frame == len(h_list):
            frame = 0
        return cur_time


start_time = pygame.time.get_ticks()
animation_cooldown_full_hearts = 250
animation_cooldown_half_hearts = 100
animation_cooldown_full_armor = 325

frame_fulls = 0
frame_halves = 0
frame_farm = 0

full_hearts_list = make_animation_list(fhs, full_hearts.get_width())
half_hearts_list = make_animation_list(hhs, half_hearts.get_width())
full_armor_list = make_animation_list(ahs, armor_hearts.get_width())

moving_left = False
moving_right = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    screen.blit(main_bkg, (0,0))
    screen.blit(main_bkg2, (512,0))
    screen.blit(main_bkg, (1024,0))
    screen.blit(moon, (250,0))
    screen.blit(stick_fucker, (300,350))
    # pygame.draw.rect(screen, BLACK, pygame.Rect(300,350,128,128))

    current_time = pygame.time.get_ticks()
    last_update_fulls = animation_update(start_time, current_time, animation_cooldown_full_hearts, full_hearts_list)
    last_update_halves = animation_update(start_time, current_time, animation_cooldown_half_hearts, half_hearts_list)
    last_update_full_arm = animation_update(start_time, current_time, animation_cooldown_full_armor, full_armor_list)

    shift_coeff = -35
    shift_coeff_full_arm = -35
    for shift in range(4):
        screen.blit(full_hearts_list[frame_fulls],(shift_coeff,-40))
        screen.blit(half_hearts_list[frame_halves],(shift_coeff, 0))
        screen.blit(full_armor_list[frame_farm],(shift_coeff_full_arm, 50))
        shift_coeff += 40
        shift_coeff_full_arm += 60
    pygame.display.update()
pygame.quit()