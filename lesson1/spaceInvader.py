import math
import random
import pygame 

SCREENWITDTH = 800
SCREENHEIGHT = 500
PLAYERSTART_X = 370
PLAYERSTART_Y = 480
ENEMYSTART_Y_MIN = 50
ENEMYSTART_Y_MAX = 150
ENEMY_SPEED_X = 4 
ENEMY_SPEED_Y = 40
BULLETSPEED_X = 10
BULLETSPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.init()

screen = pygame.display.set_mode((SCREENWITDTH, SCREENHEIGHT))
background = pygame.image.load("background.png")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.png")
playerX = PLAYERSTART_X
playerY = PLAYERSTART_Y
playerX_change = 0
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies) :
    enemyIMG.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, SCREENWITDTH - 64))
    enemyY.append(random.randint(ENEMYSTART_Y_MIN, ENEMYSTART_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = PLAYERSTART_Y
bulletX_change = 0
bulletY_change = BULLETSPEED_Y
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < COLLISION_DISTANCE
running = True
while running:
    screen.fill((0 , 0 , 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                #player movement
                playerX += playerX_change
                playerX = max(0, min(playerX, SCREENWITDTH - 64))
    for i in range(num_of_enemies) :
      if enemyY[i] > 340 :
          for j in range(num_of_enemies) :
              enemyY[j] = 2000
          game_over_text()
          break
      enemyX[i] += enemyX_change[i]
      if enemyX[i] <= 0 or enemyX[i] >= SCREENWITDTH - 64 :
          enemyX_change[i]*= -1
          enemyY[i] += enemyY_change[i]
      if isCollision(enemyX[i] , enemyY[i] , bulletX , bulletY) :
          bulletY = PLAYERSTART_Y
          bullet_state = 'ready'
          score_value += 1
          enemyX[i] = random.randint(0 , SCREENWITDTH - 64)
          enemyY[i] = random.randint(ENEMYSTART_Y_MIN , ENEMYSTART_Y_MAX)
          enemy(enemyX[i] , enemyY[i] , i)
      if bulletY <= 0 :
          bulletY = PLAYERSTART_Y
          bullet_state = 'ready'
      elif  bullet_state == 'fire' :
          fire_bullet(bulletX , bulletY)
          bulletY -= bulletY_change
      player(playerX , playerY)
      show_score(textX , textY)
      pygame.display.flip()
 
 