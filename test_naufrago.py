import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
# GRAY = (192, 192, 192)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
CELL_SIZE = 70
#dimension del tablero
BOARD_WIDTH = 4
BOARD_HEIGHT = 4

# Cargar imágenes
background = pygame.image.load('images/ocean.jpg')
naufrago_png = pygame.image.load('images/naufrago.png')
ola = pygame.image.load('images/ola.jpeg')

# Calcular el tamaño de la ventana
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Crear la ventana
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Buscando a los Náufragos")
font = pygame.font.Font('freesansbold.ttf', 18)

# Función para dibujar el tablero
def draw_board(tablero, marcados, naufragos_encontrados_pos):
    for y, row in enumerate(tablero):
        for x in range(len(row)): 
            # Calcular la posición y el tamaño del rectángulo que representa una celda del tablero
            rect = pygame.Rect((WINDOW_WIDTH - CELL_SIZE * BOARD_WIDTH) / 2 + x * CELL_SIZE, 
                               (WINDOW_HEIGHT - CELL_SIZE * BOARD_HEIGHT) / 2 + y * CELL_SIZE, 
                               CELL_SIZE, CELL_SIZE)
            if (y, x) in naufragos_encontrados_pos:
                # Mostrar el icono del náufrago si se ha encontrado en esta celda
                icono = pygame.transform.scale(naufrago_png, (CELL_SIZE, CELL_SIZE))
                screen.blit(icono, rect) 
            elif (y, x) in marcados:
                # Mostrar el icono de la ola si se ha marcado esta celda
                icono = pygame.transform.scale(ola, (CELL_SIZE, CELL_SIZE))
                screen.blit(icono, rect)
            else:
                # Dibujar un rectángulo blanco si la celda está vacía
                pygame.draw.rect(screen, WHITE, rect)
            # Dibujar el borde negro de cada celda del tablero
            pygame.draw.rect(screen, BLACK, rect, 1)

# Función para manejar eventos de entrada
def handle_events(tablero, intentos_restantes, marcados, naufragos_encontrados, naufragos_encontrados_pos):
    resultado = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # evento cuando se hace clic
            if intentos_restantes > 0 and naufragos_encontrados < 4:
                x, y = pygame.mouse.get_pos() # coordenadas del clic
                # Convertir las coordenadas del clic a índices de la celda en el tablero
                col = int((x - (WINDOW_WIDTH - CELL_SIZE * BOARD_WIDTH) / 2) // CELL_SIZE) 
                fil = int((y - (WINDOW_HEIGHT - CELL_SIZE * BOARD_HEIGHT) / 2) // CELL_SIZE)
                # Verificar si el clic está dentro del tablero
                if 0 <= fil < BOARD_HEIGHT and 0 <= col < BOARD_WIDTH:
                    if (fil, col) not in marcados and (fil, col) not in naufragos_encontrados_pos:
                        if tablero[fil][col] == 1:
                            # Si se ha encontrado un náufrago en esta celda
                            resultado = "¡Náufrago encontrado!"
                            naufragos_encontrados += 1
                            naufragos_encontrados_pos.add((fil, col))
                        else:
                            # Si no hay náufrago en esta celda
                            resultado = "No hay náufrago aquí."
                            marcados.add((fil, col))
                        intentos_restantes -= 1
                        if naufragos_encontrados == 4:
                            resultado = "¡Has ganado!"
                        elif intentos_restantes == 0 and naufragos_encontrados < 4:
                            resultado = "¡Has perdido!"
    return intentos_restantes, resultado, naufragos_encontrados

# Función para inicializar el tablero y los náufragos
def init_board():
    tablero = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    
    naufragos = 0
    while naufragos < 4:
        # Colocar 4 náufragos aleatoriamente en el tablero
        fil = random.randint(0, BOARD_HEIGHT - 1)
        col = random.randint(0, BOARD_WIDTH - 1)
        if tablero[fil][col] == 0:
            tablero[fil][col] = 1
            naufragos += 1
    
    return tablero

# Función para dibujar el botón de reintentar
def draw_retry_button():
    # Calcular la posición y el tamaño del botón de reintentar
    button_rect = pygame.Rect((WINDOW_WIDTH - 180) // 2, WINDOW_HEIGHT - 100, 180, 40)
    # Dibujar el botón de reintentar
    pygame.draw.rect(screen, GREEN, button_rect)
    # Renderizar el texto del botón de reintentar y centrarlo en el botón
    text = font.render("Volver a jugar", True, BLACK)
    screen.blit(text, ((button_rect.x + button_rect.width // 2 - text.get_width() // 2), 
                       (button_rect.y + button_rect.height // 2 - text.get_height() // 2)))
    return button_rect

# Función para manejar eventos del botón de reintentar
def handle_retry_button(button_rect):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se ha hecho clic en el botón de reintentar
            x, y = pygame.mouse.get_pos()
            if button_rect.collidepoint(x, y):
                return True
    return False

# Función principal del juego
def main():
    tablero = init_board()
    intentos_restantes = 10
    naufragos_encontrados = 0
    marcados = set()
    naufragos_encontrados_pos = set()
    resultado = None
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        # Si el juego ha terminado, mostrar el botón de reintentar
        if resultado in ["¡Has ganado!", "¡Has perdido!"]:
            button_rect = draw_retry_button()
            # Manejar eventos del botón de reintentar
            if handle_retry_button(button_rect):
                tablero = init_board()
                intentos_restantes = 10
                naufragos_encontrados = 0
                marcados = set()
                naufragos_encontrados_pos = set()
                resultado = None
        else:
            # Si el juego continúa, manejar eventos del tablero
            intentos_restantes, new_resultado, naufragos_encontrados = handle_events(
                tablero, intentos_restantes, marcados, naufragos_encontrados, naufragos_encontrados_pos)
            if new_resultado:
                resultado = new_resultado
        # Dibujar el tablero y otros elementos en pantalla
        draw_board(tablero, marcados, naufragos_encontrados_pos)
        text_intentos = font.render(f"Intentos restantes: {intentos_restantes}", True, BLACK)
        screen.blit(text_intentos, (50, 100))  # Dibujar el texto en la pantalla
        text_naufragos = font.render(f"Náufragos encontrados: {naufragos_encontrados}", True, BLACK)
        screen.blit(text_naufragos, (50, 150))  # Dibujar el texto en la pantalla
        if resultado:
            # Determinar el color del texto del resultado
            if resultado == "¡Has ganado!":
                color_resultado = GREEN  # Color verde para "¡Has ganado!"
            elif resultado == "¡Has perdido!":
                color_resultado = RED  # Color rojo para "¡Has perdido!"
            else:
                color_resultado = BLACK  # Color negro predeterminado
            # Renderizar y mostrar el texto del resultado con el color correspondiente
            text_resultado = font.render(resultado, True, color_resultado)
            screen.blit(text_resultado, (50, 50))
        pygame.display.flip()

# Ejecutar el juego
if __name__ == "__main__":
    main()