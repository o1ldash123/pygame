import pygame

def main():
    pygame.init()
    sWidth,sHeight = 500 , 500
    screen = pygame.display.set_mode((sWidth , sHeight))
    pygame.display.set_caption('color changing sprite')

    colors = {
        'red': pygame.Color('red') ,
        'green' : pygame.Color('green') ,
        'blue' : pygame.Color('blue') ,
        'yellow' : pygame.Color('yellow') ,
        'white' : pygame.Color('white')
    }

    currentClr = colors['white']
    x , y = 30 ,30
    spWidth , spHeight = 60 ,60
    clock = pygame.time.Clock()

    done = False
    while not done :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] : x -= 3
        if pressed[pygame.K_RIGHT] : x += 3
        if pressed[pygame.K_UP] : y -= 3
        if pressed[pygame.K_DOWN] : y += 3
        x = min(max(0 , x) , sWidth - spWidth)
        y = min(max(0 , y) , sHeight - spHeight)
        if x ==0 : currentClr = colors['blue']
        elif x == sWidth -spWidth : currentClr = colors['yellow']
        elif y == 0 : currentClr = colors['red']
        elif y == sHeight - spHeight :
            currentClr = colors['green']
        else :
            currentClr = colors['white']
        screen.fill((0,0,0))
        pygame.draw.rect(screen , currentClr , (x , y , sWidth , sHeight))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()

if __name__ == '__main__' :
    main()