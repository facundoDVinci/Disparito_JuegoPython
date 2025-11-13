import pygame, random
from configuracion import *

def mostrar_texto(superficie, texto, tam, color, x, y):
    fuente = pygame.font.Font("PressStart2P.ttf", tam)
    render = fuente.render(texto, True, color)
    superficie.blit(render, (x, y))

def reiniciar_juego(todos, enemigos, balas, obstaculos, balas_enemigas, Nave):
    todos.empty()
    enemigos.empty()
    balas.empty()
    obstaculos.empty()
    balas_enemigas.empty()
    nave = Nave()
    todos.add(nave)
    return nave

def pantalla_inicio(VENTANA):
    fuente_titulo = pygame.font.Font("PressStart2P.ttf", 50)
    fuente_texto = pygame.font.Font("PressStart2P.ttf", 20)
    fuente_input = pygame.font.Font("PressStart2P.ttf", 17)
    reloj = pygame.time.Clock()
    nombre = ""
    activo = True
    parpadeo = True
    timer = 0


    estrellas = []
    for _ in range(80):
        x = random.randint(0, ANCHO)
        y = random.randint(0, ALTO)
        velocidad = random.uniform(1, 3)
        estrellas.append([x, y, velocidad])

    while True:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre.strip() != "":
                    return nombre  # ← devolvemos el nombre
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif evento.unicode.isprintable() and len(nombre) < 12:
                    nombre += evento.unicode

       
        VENTANA.fill((NEGRO))
        for estrella in estrellas:
            pygame.draw.circle(VENTANA, (255, 255, 255), (int(estrella[0]), int(estrella[1])), 2)
            estrella[0] -= estrella[2]
            if estrella[0] < 0:
                estrella[0] = ANCHO
                estrella[1] = random.randint(0, ALTO)

       
        timer += 1
        if timer % 30 == 0:
            parpadeo = not parpadeo

       
        if parpadeo:
            texto_titulo = fuente_titulo.render("DISPARITO", True, (255, 255, 255))
            VENTANA.blit(texto_titulo, (ANCHO // 4, 150))

        
        pygame.draw.rect(VENTANA, (255, 255, 255), (ANCHO // 2 - 160, 350, 320, 40), 2)
        texto_input = fuente_input.render(nombre, True, (255, 255, 0))
        VENTANA.blit(texto_input, (ANCHO // 2 - 150, 355))

        texto_info = fuente_texto.render("ESCRIBE TU NOMBRE Y PULSA ENTER", True, (0, 255, 200))
        VENTANA.blit(texto_info, (ANCHO // 2 - 270, 420))

        pygame.display.flip()

