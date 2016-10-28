#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 864#940
HEIGHT = 540
 
# Clases
# ---------------------------------------------------------------------
 
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/ball3.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]
 
    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    #.......................
    hierba = pygame.image.load('images/HIERBA.png')
    fondo = load_image('images/FONDO.png')
    nubes = load_image('images/NUBES.png', transparent=True)
    sol = load_image('images/sol.png', transparent=True)
    background_size = fondo.get_size()
    background_rect = fondo.get_rect()
    screen = pygame.display.set_mode(background_size)
    w,h = background_size

    #...................... 
    bola = Bola()
    clock = pygame.time.Clock()
    x = 0
    y = 0
    x1 = -w*2
    y1 = 0
    n = 0
    s = 0
    while True:
        x1 -= 5
        x -= 5
        time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                 sys.exit(0)
 
        bola.actualizar(time)
        screen.blit(fondo, (0, 0))
        if x < -w:
            x = w
        if x1 < -w:
            x1 = w
        #screen.blit(sol, (s, 0))
        screen.blit(nubes, (n, 0))
        n -= 1
        if n < -w:
            n = w

        screen.blit(hierba, (x, y))
        screen.blit(hierba,(x1,y1))
        s -= 0.5
        if s < -w:
            s = w
        screen.blit(bola.image, bola.rect)
        pygame.display.update()
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
