import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solitario")

# Colores
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)

# Cargar imágenes de cartas (puedes reemplazar con tus propias imágenes)
CARD_BACK = pygame.Surface((100, 150))
CARD_BACK.fill(WHITE)

# Crear una baraja de cartas
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
random.shuffle(deck)

# Bucle principal del juego
running = True
while running:
    screen.fill(GREEN)
    
    # Dibujar una carta como ejemplo
    screen.blit(CARD_BACK, (350, 225))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
