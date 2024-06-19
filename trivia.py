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
font = pygame.font.Font(None, 18)

# Categorías
categories = ['Python', 'JavaScript', 'Java', 'C']
colors = [RED, GREEN, BLUE , BLACK]

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

def draw_wheel():
    center = (WIDTH // 2, HEIGHT // 2)
    radius = 200
    angle = 360 / len(categories)

    for i, category in enumerate(categories):
        start_angle = math.radians(i * angle)
        end_angle = math.radians((i + 1) * angle)
        pygame.draw.arc(screen, colors[i], [center[0] - radius, center[1] - radius, radius * 2, radius * 2], start_angle, end_angle, radius)
        mid_angle = (start_angle + end_angle) / 2
        text_x = center[0] + int(radius / 1.5 * math.cos(mid_angle))
        text_y = center[1] + int(radius / 1.5 * math.sin(mid_angle))
        draw_text(category, font, BLACK, screen, text_x - 20, text_y - 10)

def spin_wheel():
    selected_category = random.choice(categories)
    total_spins = random.randint(5, 10)  # Número total de vueltas que dará la ruleta
    current_spin = 0
    angle = 0
    spin_speed = 20  # Ajustar la velocidad de giro

    while current_spin < total_spins * 360:
        screen.fill(WHITE)
        draw_wheel()

        rotated_surface = pygame.transform.rotate(screen, angle)
        rect = rotated_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(rotated_surface, rect.topleft)
        
        pygame.display.update()

        angle += spin_speed
        current_spin += spin_speed
        pygame.time.delay(20)  # Reducir el delay para hacer la ruleta más rápida

    # Ajustar el ángulo final para que caiga en la categoría seleccionada
    selected_index = categories.index(selected_category)
    final_angle = selected_index * (360 // len(categories))
    while angle % 360 != final_angle:
        screen.fill(WHITE)
        draw_wheel()

        rotated_surface = pygame.transform.rotate(screen, angle)
        rect = rotated_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(rotated_surface, rect.topleft)
        
        pygame.display.update()

        angle += spin_speed
        pygame.time.delay(20)  # Reducir el delay para hacer la ruleta más rápida

    return selected_category

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text('TriviaTrack', font, BLACK, screen, 20, 20)
        draw_text('Presiona ESPACIO para girar la ruleta', font, BLACK, screen, 20, 100)
        draw_wheel()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    selected_category = spin_wheel()
                    game_loop(selected_category)

        pygame.display.update()

def game_loop(category):
    questions = get_questions(category)
    score = 0
    question_index = 0

    while True:
        screen.fill(WHITE)
        if question_index < len(questions):
            question, options, correct_option = questions[question_index]
            draw_text(f'Pregunta: {question}', font, BLACK, screen, 20, 20)
            for i, option in enumerate(options):
                draw_text(f'{i + 1}. {option}', font, BLACK, screen, 20, 100 + i * 40)
        
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
                            score += 1
                        question_index += 1
        else:
            screen.fill(WHITE)
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
