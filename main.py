import pygame
import random
import math
# youssef adel
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
enemys = []
enemy_x = []
enemy_y = []
enemy_xchange = []
enemy_ychange = []
num_of_enemies = 10
for j in range(num_of_enemies):
    enemys.append(pygame.image.load("alien-pixelated-shape-of-a-digital-game.png"))
    enemy_x.append(random.randint(0, 900))
    enemy_y.append(random.randint(20, 50))
    enemy_xchange.append(2.5)
    enemy_ychange.append(60)

# bullet================================================================================
bullet_img = pygame.image.load("laser.png")
bullet_x = 0
bullet_y = 510
bullet_ychange = -10
bullet_state = "rest"

# score====================================================================================

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 22)
textX = 10
textY = 10

# Game Over text============================================================================
over_font = pygame.font.Font("freesansbold.ttf", 64)


# game functions
def player(x, y):
    main_screen.blit(player_img, (x, y))


# ==============================

def enemy(x, y, j):
    main_screen.blit(enemys[j], (x, y))


# =================================
def iscollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# ===========================
def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    main_screen.blit(bullet_img, (x, y + 5))


# =============================================
def Game_Over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    main_screen.blit(over_text, (200, 250))


# ============================================
def show_score(x, y):
    score = font.render("score:" + str(score_value), True, (255, 255, 255))
    main_screen.blit(score, (x, y))


# color of main screen
color = (43, 43, 230)  # RGB format

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
                player_change = -4
            if events.key == pygame.K_RIGHT:
                player_change = 4
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

    # bullet fire
    if bullet_y <= 0:
        bullet_state = "rest"
        bullet_y = 510
        bullet_x = 0
    if bullet_state == "fire":
        bullet(bullet_x, bullet_y)
        bullet_y += bullet_ychange
    # enemy
        # Game Over
    for j in range(num_of_enemies):
         if enemy_y[j] > 600:
             enemy_y[j] = 2000
             Game_Over()
             break

    enemy_y[j] += enemy_ychange[j]
    if enemy_y[j] <= 0:
        enemy_xchange[j] = 2
        enemy_y[j] += enemy_ychange[j]
    elif enemy_x[j] >= 900:
        enemy_xchange[j] = -2
        enemy_y[j] += enemy_ychange[j]

    # collision
    collision = iscollision(enemy_x[j], enemy_y[j], bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = "rest"
        score_value += 1
        enemy_x[j] = random.randint(0, 735)
        enemy_y[j] = random.randint(100, 250)
        enemy(enemy_x[j], enemy_y[j], j)

    # ============== call_funtion ========================
    player(player_x, player_y)

    enemy(enemy_x[j], enemy_y[j], j)

    show_score(textX, textY)
    pygame.display.update()
