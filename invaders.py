import pygame
import random
from pygame import mixer

# intialize_pygame
pygame.init()
# background
background = pygame.image.load("background.jpg")
# muscic
laser = mixer.Sound("shoot.wav")


# player================================================================================
player_x = 450  # player postion to wight
player_y = 530  # player postion to hight#i did this to conrtol its movement
player_change = 0
player_img = pygame.image.load("space-invaders.png")
# Enemy================================================================================
numofenemies = 20
enemys = []
enemy_x = []
enemy_y = []
enemy_xchange = []
enemy_ychange = []
for i in range(numofenemies):
    enemys.append(pygame.image.load("alien-pixelated-shape-of-a-digital-game.png"))
    enemy_x.append(random.randint(0, 900))
    enemy_y.append(random.randint(20, 50))
    enemy_xchange.append(2.5)
    enemy_ychange.append(60)

# bullet================================================================================
bullet_img = pygame.image.load("laser.png")
bullet_x = 0
bullet_y = 510
bullet_ychange = -5
bullet_state = "rest"


# game functions
def player(x, y):
    main_screen.blit(player_img, (x, y))


# ==============================

def enemy(x, y, i):
    main_screen.blit(enemys[i], (x, y))


# ===========================
def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    main_screen.blit(bullet_img, (x, y + 5))


# color of main screen
color = (43, 43, 230)  # RGB format
# back ground
# background = pygame.image.load("invaderbackground.jpg")
# sound

# main screen
main_screen = pygame.display.set_mode((900, 600))  # x=wight=900 and y= hight = 700
pygame.display.set_caption("Welcome to Space Invaders")  # Title appers at the top
pygame.display.set_icon(pygame.image.load("alien.png"))  # icon of alien
# icon of alien
# game loop#
on = True
while on:
    main_screen.fill(color)
    main_screen.blit(background, (0, 0))
    on = True  # to make nolimit loop
    # loop to all events
    for events in pygame.event.get():  # controll_ever thing in game
        if events.type == pygame.QUIT:  # trun_off screen make cross work
            on = False
        # =========================================================
        # game controls
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                player_change = -3
            if events.key == pygame.K_RIGHT:
                player_change = 3
            if events.key == pygame.K_SPACE:
                if bullet_state == "rest":
                    bullet_x = player_x
                    bullet(bullet_x, bullet_y)
                    laser.get_volume()
                    laser.play()

        if events.type == pygame.KEYUP:
            if events.type == pygame.K_RIGHT or pygame.K_LEFT:
                player_change = 0

    # borders
    player_x += player_change
    if player_x >= 900:
        player_x -= 50
    elif player_x <= 0:
        player_x += 60
    # enemy movement
    enemy_x[i] += enemy_xchange[i]
    if enemy_x[i] <= 0:
        enemy_xchange[i] = 4
        enemy_y[i] += enemy_ychange[i]
    elif enemy_x[i] >= 900:
        enemy_y[i] += enemy_ychange[i]
        enemy_xchange[i] = -4
    # bullet fire
    if bullet_y <= 0:
        bullet_state = "rest"
        bullet_y = 510
        bullet_x = 0
    if bullet_state == "fire":
        bullet(bullet_x, bullet_y)
        bullet_y += bullet_ychange

    # ============== call_funtion ========================
    player(player_x, player_y)
    enemy(enemy_x[i], enemy_y[i], i)
    pygame.display.update()
