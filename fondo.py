import pygame, random
from configuracion import ANCHO, ALTO

class FondoEstrellas:
    def __init__(self, cantidad=80):
        self.estrellas = []
        for _ in range(cantidad):
            x = random.randint(0, ANCHO)
            y = random.randint(0, ALTO)
            velocidad = random.uniform(1, 4)
            tamaño = random.randint(1, 3)
            color = (255, 255, 255)
            self.estrellas.append([x, y, velocidad, tamaño, color])

    def update(self):
        for estrella in self.estrellas:
            estrella[0] -= estrella[2]
            if estrella[0] < 0:
                estrella[0] = ANCHO
                estrella[1] = random.randint(0, ALTO)
                estrella[2] = random.uniform(1, 4)
                estrella[3] = random.randint(1, 3)

    def draw(self, superficie):
        for estrella in self.estrellas:
            pygame.draw.circle(superficie, estrella[4], (int(estrella[0]), int(estrella[1])), estrella[3])
