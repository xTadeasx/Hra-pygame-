import pygame
import random

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jahody na útěku")

#nastavení
pohyb = 10
fps = 60
clock = pygame.time.Clock()
score = 0
lvl = 0

#barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#font
font_jahody = pygame.font.SysFont("arial", 30)
jahody_text = font_jahody.render("Jahody na útěku", True, blue)
jahody_text_rect = jahody_text.get_rect()
jahody_text_rect.centerx = width//2
jahody_text_rect.top = 5

#obrázky
worm_image = pygame.image.load("obrázky/worm.png")
worm_rect = worm_image.get_rect()
worm_rect.center = (width//2, height//2)

jahoda_image = pygame.image.load("obrázky/strawberry.png")
jahoda_rect = jahoda_image.get_rect()
jahoda_rect.center = (100, 250)

sign_image = pygame.image.load("obrázky/sign.png")
sign_rect = sign_image.get_rect()
sign_rect.center = (width-16, 300)

sign_rect2 = sign_image.get_rect()
sign_rect2.center = (300, height)

sign_rect3 = sign_image.get_rect()
sign_rect3.center = (width-16, 200)

sign_rect4 = sign_image.get_rect()
sign_rect4.center = (200, height)

#hudba v pozadí
pygame.mixer.music.load("songy/sound.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

#zvuky
zvuk = pygame.mixer.Sound("songy/pick.wav")


Hra = True
while Hra:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Hra = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP]) and worm_rect.top > 50 or (keys[pygame.K_w]) and worm_rect.top > 50:
        worm_rect.y -= pohyb
    elif (keys[pygame.K_DOWN]) and worm_rect.bottom < height or (keys[pygame.K_s]) and worm_rect.bottom < height:
        worm_rect.y += pohyb
    elif (keys[pygame.K_LEFT]) and worm_rect.left > 0 or (keys[pygame.K_a]) and worm_rect.left > 0:
        worm_rect.x -= pohyb
    elif (keys[pygame.K_RIGHT]) and worm_rect.right < width or (keys[pygame.K_d]) and worm_rect.right < width:
        worm_rect.x += pohyb

    # kolize

    if worm_rect.colliderect(jahoda_rect):
        jahoda_rect.centerx = random.randint(16, width - 16)
        jahoda_rect.centery = random.randint(66, 500 - 16)
        score += 1
        zvuk.play()

    if worm_rect.colliderect(sign_rect):
        score = 0
    elif worm_rect.colliderect(sign_rect2):
        score = 0
    elif worm_rect.colliderect(sign_rect3):
        score = 0
    elif worm_rect.colliderect(sign_rect4):
        score = 0

    #překážka

    if sign_rect.x <= 0:
        random_cislo = random.randint(0,1)
        if random_cislo == 1:
            sign_rect.y = random.randint(50,250)
        elif random_cislo == 0:
            sign_rect.y = random.randint(250, 490)
        sign_rect.x = width

    sign_rect.x -= 5

    if sign_rect2.y <= 50:
        random_cislo = random.randint(0,1)
        if random_cislo == 1:
            sign_rect2.x = random.randint(0,500)
        elif random_cislo == 0:
            sign_rect2.x = random.randint(500, width)
        sign_rect2.y = height

    sign_rect2.y -= 5

    if sign_rect3.x <= 0:
        random_cislo = random.randint(0,1)
        if random_cislo == 1:
            sign_rect3.y = random.randint(50,250)
        elif random_cislo == 0:
            sign_rect3.y = random.randint(250, 500)
        sign_rect3.x = width

    sign_rect3.x -= 5

    if sign_rect4.y <= 50:
        random_cislo = random.randint(0,1)
        if random_cislo == 1:
            sign_rect4.x = random.randint(0,490)
        elif random_cislo == 0:
            sign_rect4.x = random.randint(500, width)
        sign_rect4.y = height

    sign_rect4.y -= 5





    # vyplnění obrazovky
    screen.fill(black)

    #tvaraa
    pygame.draw.line(screen, blue, (0, 50), (width, 50), 2)

    #text
    score_text = font_jahody.render(f"score: {score}", True, blue)
    score_text_rect = score_text.get_rect()
    score_text_rect.x = 10
    score_text_rect.y = 10

    lvl_text = font_jahody.render(f"level: {lvl}", True, blue)
    lvl_text_rect = lvl_text.get_rect()
    lvl_text_rect.x = 900
    lvl_text_rect.y = 10

    # přidání obrázků
    screen.blit(worm_image, worm_rect)
    screen.blit(jahoda_image, jahoda_rect)
    screen.blit(jahody_text, jahody_text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(lvl_text, lvl_text_rect)
    screen.blit(sign_image, sign_rect)
    screen.blit(sign_image, sign_rect2)

    if score == 10:
        lvl += 1
        score = 0
    if lvl >= 1:
        screen.blit(sign_image, sign_rect3)
        screen.blit(sign_image, sign_rect4)

    # Updat obrazu
    pygame.display.update()

    #hodiny
    clock.tick(fps)

pygame.quit()
