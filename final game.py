import pygame
import random
import math
from pygame import mixer

# Intialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((900, 600))

# Background
background = pygame.image.load("background.jpg")

# Background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# icon and title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("space-game-character-of-pixels.png"))
    enemyImg.append(pygame.image.load("32288-3-space-invaders_32x32.ico"))
    enemyImg.append(pygame.image.load("32282-4-space-invaders-free-download_32x32.ico"))
    enemyX.append(random.randint(0, 890))
    enemyY.append(random.randint(70, 100))
    enemyX_change.append(0.5)
    enemyY_change.append(20)

# Bullet================================
bulletImg = pygame.image.load("laser.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"

# score===================================
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

# Game Over text=============================================
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Winner====================================================
win_font = pygame.font.Font("freesansbold.ttf", 64)

# Motivation=================================================
motivation_font = pygame.font.Font("freesansbold.ttf", 64)

#functions====================================================
def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def Game_Over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (220, 250))


def Winner():
    win_text = win_font.render("WINNER", True, (255, 255, 255))
    screen.blit(win_text, (260, 250))


def Motivation():
    over_text = over_font.render("GO ON", True, (255, 255, 255))
    screen.blit(over_text, (260, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.sqrt(math.pow(enemyY - bulletY, 2)))
    if distance < 100:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB Red Green Blue
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("shoot.wav")
                    bullet_sound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    # Checking for boundaries of spaceship so it does not go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] >= 600:
            for j in range(num_of_enemies):
                enemyY[i] = 2000
            Game_Over()
            break

        # Winner
        if score_value == 50:
            Winner()
            break

        # Motivation
        if score_value == 10 or score_value == 20 or score_value == 30 or score_value == 40:
            Motivation()

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 900:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = Collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 900)
            enemyY[i] = random.randint(60, 100)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
#call functions==========================
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()