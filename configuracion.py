import pygame

pygame.init()

ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("disparito (prototipo)")

FPS = 60
RELOJ = pygame.time.Clock()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 150, 255)
AMARILLO = (255, 255, 0)
GRIS = (100, 100, 100)