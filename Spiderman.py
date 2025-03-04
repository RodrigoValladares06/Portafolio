import pygame
import random
import os

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 600, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Spiderman: Esquiva y Atrapa")

# Cambiar al directorio del script para evitar errores con imágenes
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cargar imágenes
spiderman = pygame.image.load("spiderman.png")
spiderman = pygame.transform.scale(spiderman, (80, 80))
web = pygame.image.load("web.png")
web = pygame.transform.scale(web, (40, 40))
enemigo = pygame.image.load("enemigo.png")
enemigo = pygame.transform.scale(enemigo, (60, 60))

# Colores
BLANCO = (255, 255, 255)

# Variables del juego
spiderman_x = ANCHO // 2 - 40
spiderman_y = ALTO - 100
velocidad = 8

# Listas de objetos
telarañas = []
enemigos = []
puntuacion = 0

# Reloj
clock = pygame.time.Clock()

# Bucle principal
ejecutando = True
while ejecutando:
    pantalla.fill(BLANCO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    
    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and spiderman_x > 0:
        spiderman_x -= velocidad
    if teclas[pygame.K_RIGHT] and spiderman_x < ANCHO - 80:
        spiderman_x += velocidad
    
    # Generar objetos
    if random.randint(1, 30) == 1:
        telarañas.append([random.randint(0, ANCHO - 40), 0])
    if random.randint(1, 50) == 1:
        enemigos.append([random.randint(0, ANCHO - 60), 0])
    
    # Mover y dibujar objetos
    for t in telarañas[:]:
        t[1] += 5
        pantalla.blit(web, (t[0], t[1]))
        if t[1] > ALTO:
            telarañas.remove(t)
        if pygame.Rect(t[0], t[1], 40, 40).colliderect(spiderman_x, spiderman_y, 80, 80):
            telarañas.remove(t)
            puntuacion += 1
    
    for e in enemigos[:]:
        e[1] += 7
        pantalla.blit(enemigo, (e[0], e[1]))
        if e[1] > ALTO:
            enemigos.remove(e)
        if pygame.Rect(e[0], e[1], 60, 60).colliderect(spiderman_x, spiderman_y, 80, 80):
            print(f"¡Perdiste! Puntuación: {puntuacion}")
            ejecutando = False
    
    # Dibujar Spiderman
    pantalla.blit(spiderman, (spiderman_x, spiderman_y))
    
    # Mostrar puntuación
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (0, 0, 0))
    pantalla.blit(texto, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
