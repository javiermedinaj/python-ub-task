import pygame
import sys
import json
import random
import math

pygame.init()

# Configuraciones de pantalla
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TriviaTrack")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fuente
font = pygame.font.Font(None, 26)

# Cargar imagen de fondo
background = pygame.image.load('trivia/background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Categorías y archivos de imágenes correspondientes
categories = ['Python', 'JavaScript', 'Java', 'C']
image_files = ['trivia/Py.png', 'trivia/jscr.png', 'trivia/java.png', 'trivia/C.png']

# Función para cargar las imágenes y escalarlas
def load_and_scale_image(filename, size):
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, size)

# Cargar y escalar las imágenes para cada categoría de lenguaje de programación
scaled_images = [load_and_scale_image(filename, (100, 100)) for filename in image_files]

# Función para mostrar texto en la pantalla
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(text, font, color, surface, x, y, w, h):
    pygame.draw.rect(surface, color, (x, y, w, h))
    draw_text(text, font, WHITE, surface, x + 10, y + 10)
    return pygame.Rect(x, y, w, h)

def draw_wheel(surface):
    center = (WIDTH // 2, HEIGHT // 2)
    radius = 200
    angle = 360 / len(categories)

    for i, image in enumerate(scaled_images):
        start_angle = math.radians(i * angle)
        end_angle = math.radians((i + 1) * angle)

        # Calcular la posición de la imagen
        image_rect = image.get_rect()
        image_rect.center = (
            center[0] + int(radius / 1.5 * math.cos(start_angle + (angle / 2))),
            center[1] + int(radius / 1.5 * math.sin(start_angle + (angle / 2)))
        )

        surface.blit(image, image_rect)

def spin_wheel():
    selected_category = random.choice(categories)
    total_spins = random.randint(5, 10)  # Número total de vueltas que dará la ruleta
    current_spin = 0
    angle = 0
    spin_speed = 10  # Ajustar la velocidad de giro

    # Crear una superficie para la ruleta
    wheel_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    wheel_rect = wheel_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    while current_spin < total_spins * 360:
        screen.blit(background, (0, 0))
        wheel_surface.fill((0, 0, 0, 0))  # Limpiar la superficie de la ruleta
        draw_wheel(wheel_surface)

        rotated_surface = pygame.transform.rotate(wheel_surface, angle)
        rect = rotated_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(rotated_surface, rect.topleft)
        
        pygame.display.update()

        angle += spin_speed
        current_spin += spin_speed
        pygame.time.delay(10)  # Reducir el delay para hacer la ruleta más rápida

    # Ajustar el ángulo final para que caiga en la categoría seleccionada
    selected_index = categories.index(selected_category)
    final_angle = selected_index * (360 // len(categories))
    while angle % 360 != final_angle:
        screen.blit(background, (0, 0))
        wheel_surface.fill((0, 0, 0, 0))  # Limpiar la superficie de la ruleta
        draw_wheel(wheel_surface)

        rotated_surface = pygame.transform.rotate(wheel_surface, angle)
        rect = rotated_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(rotated_surface, rect.topleft)
        
        pygame.display.update()

        angle += spin_speed
        pygame.time.delay(10)  # Reducir el delay para hacer la ruleta más rápida

    return selected_category

def main_menu():
    while True:
        screen.blit(background, (0, 0))
        draw_text('TriviaTrack', font, BLACK, screen, 20, 20)
        draw_text('Presiona ESPACIO para girar la ruleta', font, BLACK, screen, 20, 100)

        # Crear una superficie para la ruleta
        wheel_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        draw_wheel(wheel_surface)
        screen.blit(wheel_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    selected_category = spin_wheel()
                    game_loop(selected_category)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit() 
                
        pygame.display.update()

def game_loop(category):
    questions = get_questions(category)
    score = 0
    question_index = 0

    while True:
        screen.blit(background, (0, 0))
        if question_index < len(questions):
            question, options, correct_option = questions[question_index]
            
            # Dibujar el cuadro para la pregunta
            pygame.draw.rect(screen, WHITE, (100, 100, 700, 400), 0)
            pygame.draw.rect(screen, BLACK, (100, 100, 700, 400), 2)

            draw_text(f'Pregunta: {question}', font, BLACK, screen, 120, 120)
            for i, option in enumerate(options):
                draw_text(f'{i + 1}. {option}', font, BLACK, screen, 120, 200 + i * 40)
        
            selected_option = None  # Inicializar la variable antes de usarla
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_option = 1
                    elif event.key == pygame.K_2:
                        selected_option = 2
                    elif event.key == pygame.K_3:
                        selected_option = 3
                    elif event.key == pygame.K_4:
                        selected_option = 4

                    if selected_option is not None:
                        if selected_option == correct_option:
                            # Mostrar la opción correcta en verde por un breve momento
                            screen.blit(background, (0, 0))
                            pygame.draw.rect(screen, WHITE, (100, 100, 700, 400), 0)
                            pygame.draw.rect(screen, BLACK, (100, 100, 700, 400), 2)
                            draw_text(f'Pregunta: {question}', font, BLACK, screen, 120, 140)
                            for i, option in enumerate(options):
                                if i + 1 == correct_option:
                                    draw_text(f'{i + 1}. {option}', font, GREEN, screen, 120, 200 + i * 40)
                                else:
                                    draw_text(f'{i + 1}. {option}', font, BLACK, screen, 120, 200 + i * 40)
                            pygame.display.update()
                            pygame.time.delay(1000)  # Esperar un segundo
                            score += 1
                            question_index += 1
                        else:
                            # Mostrar la opción incorrecta en rojo por un breve momento
                            screen.blit(background, (0, 0))
                            pygame.draw.rect(screen, WHITE, (100, 100, 700, 400), 0)
                            pygame.draw.rect(screen, BLACK, (100, 100, 700, 400), 2)
                            draw_text(f'Pregunta: {question}', font, BLACK, screen, 120, 120)
                            for i, option in enumerate(options):
                                if i + 1 == selected_option:
                                    draw_text(f'{i + 1}. {option}', font, RED, screen, 120, 200 + i * 40)
                                elif i + 1 == correct_option:
                                    draw_text(f'{i + 1}. {option}', font, GREEN, screen, 120, 200 + i * 40)
                                else:
                                    draw_text(f'{i + 1}. {option}', font, BLACK, screen, 120, 200 + i * 40)
                            pygame.display.update()
                            pygame.time.delay(1000)  # Esperar un segundo
                            question_index += 1
        else:
            screen.blit(background, (0, 0))
            draw_text(f'Fin del juego! Tu puntuación es: {score}', font, BLACK, screen, 20, 20)
            button_rect = draw_button('Volver a jugar', font, BLACK, screen, WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        return  # Salir de game_loop y volver al menú principal

        pygame.display.update()

def get_questions(category):
    with open('questions.json', 'r') as file:
        data = json.load(file)
    
    questions = []
    for item in data:
        if item['category'] == category:
            question = item['question']
            options = [item['correct_answer']] + item['incorrect_answers']
            random.shuffle(options)  # Mezclar las opciones para más variabilidad
            correct_option = options.index(item['correct_answer']) + 1
            questions.append((question, options, correct_option))
    return questions

if __name__ == "__main__":
    main_menu()
