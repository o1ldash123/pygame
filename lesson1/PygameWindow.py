import pygame 

pygame.init()

screen = pygame.display.set_mode((400 , 500))

done = False

while not done :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()

def gameLoop() :
    clock = pygame.time.Clock()
    running = True
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                runing = False
        