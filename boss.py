import pygame, random
from configuracion import ANCHO, ALTO, ROJO, BLANCO

class Boss(pygame.sprite.Sprite):
    def __init__(self, nivel, todos, balas_enemigas):
        super().__init__()
        self.image = pygame.image.load("sprites/boss.png").convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO - 200
        self.rect.centery = ALTO // 2

        
        self.hp_max = 50 + (nivel * 20)
        self.hp = self.hp_max
        self.velocidad = 3
        self.direccion = 1  
        self.cooldown = 80 - min(40, nivel * 2)  
        self.cooldown_actual = self.cooldown

        self.todos = todos
        self.balas_enemigas = balas_enemigas

    def update(self):
      
        self.rect.y += self.velocidad * self.direccion
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.direccion *= -1

      
        self.cooldown_actual -= 1
        if self.cooldown_actual <= 0:
            self.disparar()
            self.cooldown_actual = self.cooldown

    def disparar(self):
       
        cantidad_balas = 3 + min(2, self.hp_max // 100)  
        separacion_angulos = 15  
        angulo_central = 0

        for i in range(cantidad_balas):
            
            angulo = (-(cantidad_balas - 1) / 2 + i) * separacion_angulos * (3.14159 / 180)

            bala = BalaBoss(self.rect.centerx - 80, self.rect.centery, angulo)
            self.todos.add(bala)
            self.balas_enemigas.add(bala)


    def recibir_dano(self, cantidad):
        self.hp -= cantidad
        if self.hp <= 0:
            self.kill()
            return True
        return False

    def dibujar_barra_hp(self, superficie):
      
        pygame.draw.rect(superficie, (80, 0, 0), (ANCHO//2 - 150, 50, 300, 20))
   
        ancho_hp = int((self.hp / self.hp_max) * 300)
        pygame.draw.rect(superficie, ROJO, (ANCHO//2 - 150, 50, ancho_hp, 20))
 
        pygame.draw.rect(superficie, BLANCO, (ANCHO//2 - 150, 50, 300, 20), 2)


class BalaBoss(pygame.sprite.Sprite):
    def __init__(self, x, y, angulo=0):
        super().__init__()
        self.image = pygame.Surface((12, 5))
        self.image.fill((255, 60, 60))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = 5

        direccion = pygame.math.Vector2(-1, 0).rotate_rad(angulo)
        self.dx = direccion.x * self.velocidad
        self.dy = direccion.y * self.velocidad

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

       
        if self.rect.right < 0 or self.rect.top < 0 or self.rect.bottom > ALTO:
            self.kill()


