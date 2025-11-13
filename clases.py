import pygame
import random
from configuracion import *
from sonido import *

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/Jugador.png").convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.centery = ALTO // 2
        self.velocidad = 5

    def update(self, teclas=None):
        if teclas:
            if teclas[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.velocidad
            if teclas[pygame.K_DOWN] and self.rect.bottom < ALTO:
                self.rect.y += self.velocidad

    def disparar(self, balas, todos):
        disparo.play()
        bala = Bala(self.rect.right, self.rect.centery)
        balas.add(bala)
        todos.add(bala)


class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 4))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = 10

    def update(self):
        self.rect.x += self.velocidad
        if self.rect.left > ANCHO:
            self.kill()


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/Enemigo.png").convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO + random.randint(20, 100)
        self.rect.y = random.randint(20, ALTO - 40)
        self.velocidad = random.randint(3, 6)

    def update(self):
        self.rect.x -= self.velocidad
        if self.rect.right < 0:
            self.kill()


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/roca.png").convert_alpha() 
        self.rect = self.image.get_rect()
        posiciones_y = [80, ALTO // 2 - 40, ALTO - 160]
        self.rect.y = random.choice(posiciones_y)
        self.rect.x = ANCHO + random.randint(0, 100)
        self.velocidad = random.randint(4, 7)

    def update(self):
        self.rect.x -= self.velocidad
        if self.rect.right < 0:
            self.kill()


class NaveEnemiga(pygame.sprite.Sprite):
    def __init__(self, todos, balas_enemigas):
        super().__init__()
        self.image = pygame.image.load("sprites/EnemigoDisparo.png").convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO + random.randint(0, 200)
        self.rect.y = random.randint(50, ALTO - 100)
        self.velocidad = random.randint(2, 4)
        self.cooldown = random.randint(60, 120)
        self.todos = todos
        self.balas_enemigas = balas_enemigas

    def update(self):
        self.rect.x -= self.velocidad
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.disparar()
            self.cooldown = random.randint(60, 120)
        if self.rect.right < 0:
            self.kill()

    def disparar(self):
        bala = BalaEnemiga(self.rect.left, self.rect.centery)
        self.todos.add(bala)
        self.balas_enemigas.add(bala)


class BalaEnemiga(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = -8

    def update(self):
        self.rect.x += self.velocidad
        if self.rect.right < 0:
            self.kill()
