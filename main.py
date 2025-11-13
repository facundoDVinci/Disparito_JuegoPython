import pygame, sys, random
from configuracion import *
from clases import *
from funciones import mostrar_texto, reiniciar_juego, pantalla_inicio
from grupos import *
from database import inicializar_db, guardar_puntuacion, obtener_top, eliminar_datos, amigos_puntajes
from fondo import FondoEstrellas
from sonido import *
from boss import Boss  


inicializar_db()
pygame.init()


musica_de_fondo()


nombre_jugador = pantalla_inicio(VENTANA)


estado_juego = "juego"
fondo = FondoEstrellas()
nave = Nave()
todos.add(nave)

puntuacion = 0
contador_enemigo = 0
contador_enemigo2 = 0
contador_obstaculos = 0
nivel = 1
tiempo_nivel = 0
boss_activo = None  


while True:
    
    RELOJ.tick(FPS)
    teclas = pygame.key.get_pressed()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      
        if estado_juego == "juego":
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                nave.disparar(balas, todos)

    
        elif estado_juego == "gameover":
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                nombre_jugador = pantalla_inicio(VENTANA)
                estado_juego = "juego"
                nave = reiniciar_juego(todos, enemigos, balas, obstaculos, balas_enemigas, Nave)
                musica_de_fondo()
                puntuacion = 0
                nivel = 1
                tiempo_nivel = 0
                boss_activo = None

   
    if estado_juego == "juego":
        
        if boss_activo is None:
            tiempo_nivel += 1
            if tiempo_nivel % 1000 == 0:
                nivel += 1

      
        if boss_activo is None and nivel % 4 == 0 and nivel > 0:
  
            for enemigo in enemigos:
                todos.remove(enemigo)
            for obstaculo in obstaculos:
                todos.remove(obstaculo)
            enemigos.empty()
            obstaculos.empty()

            
            for bala in balas:
                todos.remove(bala)
            for bala_e in balas_enemigas:
                todos.remove(bala_e)
            balas.empty()
            balas_enemigas.empty()

           
            boss_activo = Boss(nivel, todos, balas_enemigas)
            todos.add(boss_activo)


      
        if boss_activo is None:
            contador_enemigo += 1
            if contador_enemigo > 40:
                enemigo = Enemigo()
                enemigos.add(enemigo)
                todos.add(enemigo)
                contador_enemigo = 0

            if nivel >= 2:
                contador_obstaculos += 1
                if contador_obstaculos > 120:
                    obstaculo = Obstaculo()
                    obstaculos.add(obstaculo)
                    todos.add(obstaculo)
                    contador_obstaculos = 0

            if nivel >= 3:
                contador_enemigo2 += 1
                if contador_enemigo2 > 170:
                    nave_enemiga = NaveEnemiga(todos, balas_enemigas)
                    enemigos.add(nave_enemiga)
                    todos.add(nave_enemiga)
                    contador_enemigo2 = 0

      
        fondo.update()
        nave.update(teclas)
        balas.update()
        enemigos.update()
        obstaculos.update()
        balas_enemigas.update()

        if boss_activo:
            boss_activo.update()

     
        colisiones = pygame.sprite.groupcollide(enemigos, balas, True, True)
        puntuacion += len(colisiones) * 10

      
        if boss_activo:
            hits_boss = pygame.sprite.spritecollide(boss_activo, balas, True)
            if hits_boss:
                for _ in hits_boss:
                    derrotado = boss_activo.recibir_dano(5)
                    puntuacion += 5
                    if derrotado:
                        boss_derrotado.play()
                        boss_activo = None
                        nivel += 1
                        tiempo_nivel = 0
                        break

     
        if (pygame.sprite.spritecollideany(nave, enemigos)
            or pygame.sprite.spritecollideany(nave, obstaculos)
            or pygame.sprite.spritecollideany(nave, balas_enemigas)
            or (boss_activo and pygame.sprite.collide_rect(nave, boss_activo))):
            explosion.play()
            estado_juego = "gameover"
            detener_musica()
            guardar_puntuacion(nombre_jugador, puntuacion)

      
        VENTANA.fill(NEGRO)
        fondo.draw(VENTANA)
        todos.draw(VENTANA)

        if boss_activo:
            boss_activo.dibujar_barra_hp(VENTANA)

        mostrar_texto(VENTANA, f"{nombre_jugador} | Puntos: {puntuacion} | Nivel: {nivel}", 18, BLANCO, 10, 10)


    elif estado_juego == "gameover":
        VENTANA.fill(NEGRO)
        mostrar_texto(VENTANA, "GAME OVER", 40, ROJO, ANCHO // 2 - 160, 100)
        mostrar_texto(VENTANA, f"Jugador: {nombre_jugador}", 20, BLANCO, ANCHO // 2 - 120, 200)
        mostrar_texto(VENTANA, f"Puntuación final: {puntuacion}", 20, BLANCO, ANCHO // 2 - 150, 240)
        mostrar_texto(VENTANA, "TOP 5 JUGADORES", 18, AMARILLO, ANCHO // 2 - 130, 300)

        top = obtener_top(5)
        y = 340
        for i, (nombre, puntos) in enumerate(top, start=1):
            texto = f"{i}. {nombre[:12]:12}  {puntos:>5}"
            mostrar_texto(VENTANA, texto, 18, BLANCO, ANCHO // 2 - 150, y)
            y += 30

        mostrar_texto(VENTANA, "Presione ENTER para volver al menú", 14, GRIS, ANCHO // 2 - 180, 500)
        nivel = 1

    pygame.display.flip()
