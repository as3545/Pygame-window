

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

isRunning = True

while(isRunning ==True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
