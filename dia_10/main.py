import pygame
import random
import math 
from pygame import mixer


#Inicializamos a Pygame
pygame.init()

#Crear la pantalla de vista
pantalla = pygame.display.set_mode((800, 600))
se_ejecuta = True 

#Titulo e Icono y fondo
pygame.display.set_caption("Alienigenas en la tierra")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
fondo = pygame.image.load("fondo.png")

#Agregar música
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#Variables Jugador (cohete)
cohete = pygame.image.load("astronave.png")
cohete_x = 368
cohete_y = 536
cohete_x_cambio = 0

#Variables enemigo (alien)
enemigo_s = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio =[]
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    enemigo_s.append(pygame.image.load("alienigena-aterrador.png")) 
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

    

#Variables bala (bala)
balas = pygame.image.load("balas.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 2.5
visible = False

#Variable de puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x= 10
texto_y = 10

#texto final 
fuente_final = pygame.font.Font('freesansbold.ttf', 40)


#Mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#Funcion del jugador
def jugador(x, y):
    pantalla.blit(cohete, (x, y))

#Funcion del enemigo
def enemigo(x, y, n):
    pantalla.blit(enemigo_s[n], (x, y))

#Función disparar
def disparar_bala(x,y):
    global visible
    visible = True
    pantalla.blit(balas, (x + 16, y + 10))
    
#Función mensaje final 
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

    
    
#Función detectar colisiones
def colision_f(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


#Loop de ejecución del juego
while se_ejecuta:
    
    #Fondo de la pantalla
    pantalla.blit(fondo, (0,0))

    #Iteración de eventos
    for evento in pygame.event.get():
        
        #Cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
        #Se presiono una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                cohete_x_cambio -= 1
            if evento.key == pygame.K_RIGHT:
                cohete_x_cambio += 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not visible:
                    bala_x = cohete_x
                    disparar_bala(bala_x, bala_y)
        #Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:  
                cohete_x_cambio = 0
    
    #Modificar ubicación del cohete
    cohete_x += cohete_x_cambio    
    #Mantener dentro de bordes al cohete
    if cohete_x <=0:
        cohete_x = 0
        
    elif cohete_x >= 736:
        cohete_x = 736
        
    #Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):
        
        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        
        enemigo_x[e] += enemigo_x_cambio[e] 
    #Mantener dentro de bordes al enemigo
        if enemigo_x[e]  <=0:
            enemigo_x_cambio[e]  = 0.3
            enemigo_y[e]  += enemigo_y_cambio[e] 

        elif enemigo_x[e]  >= 736:
            enemigo_x_cambio[e]  = -1
            enemigo_y[e]  += enemigo_y_cambio[e] 
            
            #colisión
        colision = colision_f(enemigo_x[e] , enemigo_y[e] , bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e]  = random.randint(0, 736)
            enemigo_y[e]  = random.randint(50, 200)
        
        enemigo(enemigo_x[e], enemigo_y[e], e)


    #Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        visible = False
        
    if visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
        

        
    jugador(cohete_x, cohete_y)
    mostrar_puntaje(texto_x, texto_y)
    
    #Actualizar programa
    pygame.display.update()
            
            
            
