import pygame

pygame.mixer.init()

disparo = pygame.mixer.Sound("sonidos/fire.wav") 
explosion = pygame.mixer.Sound("sonidos/explosion.wav")
boss_derrotado = pygame.mixer.Sound("sonidos/boss_destroyed.wav")

def musica_de_fondo():
    pygame.mixer.music.load("sonidos/fondo.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

def detener_musica():
    pygame.mixer.music.stop()
