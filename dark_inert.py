import pygame
import Player as Player
pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Darkness Inert")

main_bkg = pygame.image.load("assets/Backgrounds/bkg.jpg")
print(main_bkg.get_width(), main_bkg.get_height())
main_bkg = pygame.transform.scale(main_bkg, (main_bkg.get_width() * .125, main_bkg.get_height() * .125))
main_bkg2 = pygame.transform.flip(main_bkg,True,False)

moon = pygame.image.load("assets/Backgrounds/moon.png")
moon = pygame.transform.scale(moon, (int(moon.get_width() * 2.25), int(moon.get_height() * 2.25)))

full_hearts = pygame.image.load("assets/Hearts/hearts_sprite.png")
moving_left = False
moving_right = False
run = True

while(run):

    screen.blit(main_bkg, (0,0))
    screen.blit(main_bkg2, (512,0))
    screen.blit(main_bkg, (1024,0))
    screen.blit(moon, (350,0))
    # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(125, 225, 125, 246))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()
pygame.quit()