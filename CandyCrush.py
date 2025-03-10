import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 600
grid_size = 6
tile_size = WIDTH // grid_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush")

# Colores
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Crear la cuadrícula de caramelos
def create_grid():
    return [[random.choice(COLORS) for _ in range(grid_size)] for _ in range(grid_size)]

grid = create_grid()

# Bucle principal del juego
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Dibujar la cuadrícula de caramelos
    for row in range(grid_size):
        for col in range(grid_size):
            pygame.draw.rect(screen, grid[row][col], (col * tile_size, row * tile_size, tile_size, tile_size))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
