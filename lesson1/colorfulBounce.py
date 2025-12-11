import pygame
import random 

pygame.init()
SPRITECOLORCHANGE = pygame.USEREVENT + 1
BACKGROUNDCOLORCHANGE= pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE =  pygame.Color('darkblue')

YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE =  pygame.Color('white')
class Sprite(pygame.sprite.Sprite) :
    def __init__(self , color , height , width) :
        super().__init__()
        self.image = pygame.Surface([width , height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1 , 1]) , random.choice([-1 , 1])]
    def update(self) :
        self.rect.move_ip(self.velocity)
        boundaryHit = False
        if self.rect.left <= 0 or self.rect.right >=500 :
            self.velocity[0] = -self.velocity[0]
            boundaryHit = True
        if self.rect.top <= 0 or self.rect.bottom >=400 :
            self.velocity[1] = -self.velocity[1]
            boundaryHit = True
        if boundaryHit :
            pygame.event.post(pygame.event.Event(SPRITECOLORCHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUNDCOLORCHANGE))
    def changeCLR(self):
      self.image.fill(random.choice([YELLOW , MAGENTA , ORANGE , WHITE]))
    def changeBgColor(self) :
        global bgCol 
        bgCol = random.choice([BLUE , LIGHTBLUE , DARKBLUE])
allSprites = pygame.sprite.Group()


sp1 = Sprite(WHITE , 20 , 30)
sp1.rect.x = random.randint(0 , 370)
sp1.rect.y = random.randint(0 , 370)
allSprites.add(sp1)
screen = pygame.display.set_mode((500 , 400))
pygame.display.set_caption('Boundary sprite')
bgCol = BLUE
screen.fill(bgCol)
exit = False
clock = pygame.time.Clock()
#main game loop
while not exit :
    #event hanling loop
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit = True 
            #if sprite color change is triggered change sprite color
        elif event.type == SPRITECOLORCHANGE :
            sp1.changeCLR()
        elif event.type == BACKGROUNDCOLORCHANGE :
            print('error')
            sp1.changeBgColor()
        allSprites.update()

        screen.fill(bgCol)
        allSprites.draw(screen)
        pygame.display.flip()
        clock.tick(240)
pygame.quit()

