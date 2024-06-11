import pygame
import random

# Inicializa Pygame
pygame.init()

# Configurar la ventana de juego
screen = pygame.display.set_mode([500, 500])

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Coordenadas iniciales del jugador
player_x = 250
player_y = 250
player_speed = 5

# Coordenadas del objeto
object_x = random.randint(0, 500)
object_y = random.randint(0, 500)

# Puntuación
score = 0

# Fuente para mostrar la puntuación
font = pygame.font.Font(None, 36)

# Bucle principal
running = True
while running:
    # Gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestionar el movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Detección de colisiones
    distance = ((player_x - object_x) ** 2 + (player_y - object_y) ** 2) ** 0.5
    if distance < 40:
        score += 1
        object_x = random.randint(0, 500)
        object_y = random.randint(0, 500)

    # Rellenar el fondo de la pantalla con color blanco
    screen.fill(WHITE)

    # Dibujar el jugador (un círculo azul)
    pygame.draw.circle(screen, BLUE, (player_x, player_y), 25)

    # Dibujar el objeto (un círculo rojo)
    pygame.draw.circle(screen, RED, (object_x, object_y), 15)

    # Mostrar la puntuación
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
