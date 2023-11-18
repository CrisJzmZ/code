# -*- coding: utf-8 -*-

import pygame
import player

pygame.init()

# Definir variables

ancho_ventana = 640
alto_ventana = 480
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Jugardor moviendose")
clock = pygame.time.Clock()
player = player.Guardian((ancho_ventana/2, alto_ventana/2))
game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player.handle_event(event)
    screen.fill(pygame.Color('gray'))
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(20)

pygame.quit ()
