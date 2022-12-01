import pygame

# iniciar todas las herramientas de pygame
pygame.init()

# el tamaño se pone en una tupla entre paréntesis
pantalla = pygame.display.set_mode((800, 600))

# creamos un evento
# quit salir

se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

