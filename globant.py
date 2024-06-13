import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir constantes
ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Configurar la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escalador de Edificios")

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Cargar la imagen de fondo
fondo = pygame.image.load("images/globant.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Cargar imágenes
player_img = pygame.image.load("images/climber.png")
player_img = pygame.transform.scale(player_img, (50, 50))
enemie_img = pygame.image.load("images/bombero.gif")
enemie_img = pygame.transform.scale(enemie_img, (50, 50))
final_path = pygame.image.load("images/globant-logo.png")
final_path = pygame.transform.scale(final_path, (200, 200))

# Clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 50)
        self.velocidad_y = 0
        self.gravedad = 1
        self.puntuacion = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.velocidad_y = -5
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        
        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y

        # Colisiones con plataformas
        colisiones = pygame.sprite.spritecollide(self, plataformas, False)
        if colisiones:
            self.velocidad_y = 0
            self.rect.y = colisiones[0].rect.top - self.rect.height

        # Colisiones con bomberos
        if pygame.sprite.spritecollide(self, bomberos, False):
            self.rect.center = (ANCHO // 2, ALTO - 50)  # Reiniciar posición del jugador
            self.puntuacion = 0  # Reiniciar puntuación

        # Límite de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        # Desplazar el fondo y plataformas
        if self.rect.top < ALTO // 3:
            self.rect.y += abs(self.velocidad_y)
            for plataforma in plataformas:
                plataforma.rect.y += abs(self.velocidad_y)
                if plataforma.rect.top >= ALTO:
                    plataforma.kill()
                    # Generar una nueva plataforma en la parte superior
                    nueva_plataforma = Plataforma(random.randint(0, ANCHO - 100), -10)
                    plataformas.add(nueva_plataforma)
                    todos_los_sprites.add(nueva_plataforma)
            for bombero in bomberos:
                bombero.rect.y += abs(self.velocidad_y)
                if bombero.rect.top >= ALTO:
                    bombero.kill()
            self.puntuacion += 1

# Clase de las plataformas
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 10))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Clase de los bomberos
class Bombero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemie_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = random.choice([-3, 3])

    def update(self):
        self.rect.x += self.velocidad_x
        if self.rect.left < 0 or self.rect.right > ANCHO:
            self.velocidad_x *= -1  # Cambiar dirección

# Función para generar plataformas iniciales
def generar_plataformas_iniciales():
    for i in range(10):
        plataforma_inicial = Plataforma(random.randint(0, ANCHO - 100), random.randint(0, ALTO - 10))
        plataformas.add(plataforma_inicial)
        todos_los_sprites.add(plataforma_inicial)

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
bomberos = pygame.sprite.Group()

# Generar plataformas iniciales
generar_plataformas_iniciales()

# Crear jugador
jugador = Jugador()
todos_los_sprites.add(jugador)

# Generar bomberos
for i in range(10):
    bombero = Bombero(random.randint(0, ANCHO - 50), random.randint(10, ALTO - 10))
    bomberos.add(bombero)
    todos_los_sprites.add(bombero)

# Bucle principal del juego
ejecutando = True
mostrar_logo = False
while ejecutando:
    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar sprites
    todos_los_sprites.update()

    # Dibujar todo
    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo
    todos_los_sprites.draw(pantalla)

    # Dibujar logo al llegar a la cima
    if jugador.puntuacion >= 200:
        pantalla.blit(final_path, (ANCHO // 2 - final_path.get_width() // 2, ALTO // 2 - final_path.get_height() // 2))
        mostrar_logo = True

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar FPS
    reloj.tick(60)

# Salir del juego
pygame.quit()
