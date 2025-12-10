import pygame

pygame.init()
width , height = 500,500

displaySurface = pygame.display.set_mode((width , height))
pygame.display.set_caption('Adding image and background image')
backgroundImage = pygame.transform.scale(
    pygame.image.load('Background.png').convert , (width , height)
)
penguinImage = pygame.transform.scale(
    pygame.image.load('hllo penuin.png').convert_alpha() , (200 , 200)
)
penguinRect = penguinImage.get_rect(center = (width // 2  , height //2 - 30))

text = pygame.font.Font(None , 36).render('hellow World ' , True , pygame.Color('black'))