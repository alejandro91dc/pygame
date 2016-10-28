import pygame
import sys
import pygame.sprite as sprite

def dyn_background():
    theClock = pygame.time.Clock()
    
    background = pygame.image.load('images/FONDO.png')

    background_size = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)
    w,h = background_size
    x = 0
    y = 0

    x1 = 0
    y1 = -w

    running = True

    while running:
        screen.blit(background,background_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x1 += 5
        x += 5
        screen.blit(background,(x,y))
        screen.blit(background,(x1,y1))
        if x > w:
            x = -w
        if x1 > w:
            x1 = -w
        pygame.display.flip()
        pygame.display.update()
        theClock.tick(10)


dyn_background()
