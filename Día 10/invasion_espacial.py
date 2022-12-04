import pygame
import random
import math
from pygame import mixer


# INICIAR todas las herramientas de pygame
pygame.init()

# CREAR PANTALLA
# el tamaño se pone en una tupla entre paréntesis
pantalla = pygame.display.set_mode((800, 600))

# TÍTULO E ICONO
pygame.display.set_caption('Invasión espacial')
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# AGREGAR MÚSICA
mixer.music.load('MusicaFondo.mp3')
# bajar volumen
mixer.music.set_volume(0.3)
# -1 significa que se va a repetir cuando termine siempre
mixer.music.play(-1)

# FONDO
fondo = pygame.image.load('Fondo.jpg')

# JUGADOR
# pantalla comienza arriba a la izquierda
# coloca la imagen desde el lugar que se ponga a derecha y abajo
img_jugador = pygame.image.load("cohete.png")
# si jugador mide 64 pixels la mitad para izquierda y la mitad para arriba
# centro 800/2 - 64/2
jugador_x = 368
# alto 600 - 64/2
jugador_y = 500
# variable para controlar el movimiento
jugador_x_cambio = 0

# ENEMIGO
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# BALA
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.5
bala_visible = False

# PUNTAJE
puntaje = 0
fuente = pygame.font.Font('Fastest.ttf', 32)
texto_x = 10
texto_y = 10

# TEXTO FINAL DE JUEGO
fuente_final = pygame.font.Font('Fastest.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    # para ponerlo en el centro x 60 y 200
    pantalla.blit(mi_fuente_final, (60, 200))


# FUNCIÓN MOSTRAR PUNTAJE
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# FUNCIÓN JUGADOR
def jugador(x, y):
    # BLIT arrojar o posicionar algo
    # pide la imagen y un tupla con ancho y alto
    pantalla.blit(img_jugador, (x, y))


# FUNCIÓN ENEMIGO
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# FUNCIÓN DISPARAR BALA
def disparar_bala(x, y):
    # acceso a la variable de visibilidad de la bala
    global bala_visible
    bala_visible = True
    # para que aparezcan en el centro de la nave se le suma las mitades de la nave
    pantalla.blit(img_bala, (x + 16, y + 10))


# FUNCIÓN DETECTAR COLISIONES
# fórmula que detecta la distancia entre dos objetos
def hay_colision(x_1, y_1, x_2, y_2):
    # sqrt: raiz cuadrada
    # pow: un número al cuadrado
    distacia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distacia < 27:
        return True
    else:
        return False


# LOOP del juego
se_ejecuta = True
while se_ejecuta:

    # FONDO
    # pantalla.fill((205, 144, 228)) esto para poner un color específico
    pantalla.blit(fondo, (0, 0))

    # BUCLE QUE CONTROLA EVENTOS
    for evento in pygame.event.get():

        # EVENTO SALIR
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # EVENTO PRESIONAR TECLAS
        if evento.type == pygame.KEYDOWN:  # KEYDOWN tecla presionada
            if evento.key == pygame.K_LEFT:
                # se mueve hacia la izquierda
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                # se mueve hacia la derecha
                jugador_x_cambio = 0.1
            if evento.key == pygame.K_SPACE:
                # poner sonido a los disparos
                sonido_bala = mixer.Sound('disparo.mp3')
                # bajar sonido disparo
                mixer.Sound.set_volume(sonido_bala, 0.3)
                sonido_bala.play()

                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # EVENTO SOLTAR FLECHAS
        if evento.type == pygame.KEYUP:  # KEYUP suelta tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # MOVIMIENTO JUGADOR
    jugador_x += jugador_x_cambio

    # mantener dentro BORDES al jugador
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 736:  # 800 - 64
        jugador_x = 736

    # MODIFICAR UBICACIÓN ENEMIGO
    for e in range(cantidad_enemigos):

        # FIN DEL JUEGO
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # mantener dentro BORDES al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]

        # COLISIÓN
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            # sonido colisión
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()

            bala_y = 500  # altura de la nave
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        # ENEMIGO
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # MOVIMIENTO BALA
    # que bala desaparezca al llegar al borde
    if bala_y <= -64:  # tamaño nave como tope
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # JUGADOR
    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    # para que aparezca el color debe actualizarse la pantalla
    pygame.display.update()
