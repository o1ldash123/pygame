import pygame
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

backgroundImage = pygame.transform.scale( pygame.image.load("image.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color , height , width):
        super().__init__()
        self.image = pygame.Surface([width , height])
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image , color , pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self , xchg , ychg):
        self.rect.x =  max(min(self.rect.x + xchg, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + ychg , SCREEN_HEIGHT - self.rect.height), 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Example")
allSprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color("red"), 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
allSprites.add(sprite1)
sprite2 = Sprite(pygame.Color("green"), 20, 30) 
sprite2.rect.x , sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
allSprites.add(sprite2)
running , won = True , False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
   
    if not won :
        keys = pygame.key.get_pressed()
        xchg , ychg = 0 , 0
        if keys[pygame.K_LEFT]:
            xchg = -MOVEMENT_SPEED
        if keys[pygame.K_RIGHT]:
            xchg = MOVEMENT_SPEED
        if keys[pygame.K_UP]:
            ychg = -MOVEMENT_SPEED
        if keys[pygame.K_DOWN]:
            ychg = MOVEMENT_SPEED
        sprite1.move(xchg , ychg)
        if pygame.sprite.collide_rect(sprite1 , sprite2):
            won = True
    screen.blit(backgroundImage , (0, 0))
    allSprites.draw(screen)
    if won  :
        winText = font.render("You Win!" , True , pygame.Color("black"))
        screen.blit(winText , (SCREEN_WIDTH // 2 - winText.get_width() // 2 , SCREEN_HEIGHT // 2 - winText.get_height() // 2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()