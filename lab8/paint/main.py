import pygame
import sys
import math

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Extended Paint App")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Drawing settings
color = BLACK
radius = 5
mode = 'draw'
start_pos = None

# Fill background white
screen.fill(WHITE)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Color switching
            if event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

            # Drawing mode selection
            elif event.key == pygame.K_d:
                mode = 'draw'
            elif event.key == pygame.K_e:
                mode = 'erase'
            elif event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_t:
                mode = 'right_triangle'
            elif event.key == pygame.K_q:  # No longer using 'e' for triangle
                mode = 'equilateral_triangle'
            elif event.key == pygame.K_h:
                mode = 'rhombus'

        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            if mode == 'draw':
                pygame.draw.circle(screen, color, event.pos, radius)
            elif mode == 'erase':
                pygame.draw.circle(screen, WHITE, event.pos, radius * 2)

        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:
                if mode == 'draw':
                    pygame.draw.circle(screen, color, event.pos, radius)
                elif mode == 'erase':
                    pygame.draw.circle(screen, WHITE, event.pos, radius * 2)

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if not start_pos:
                continue

            x1, y1 = start_pos
            x2, y2 = end_pos
            dx = x2 - x1
            dy = y2 - y1

            if mode == 'rect':
                pygame.draw.rect(screen, color, pygame.Rect(x1, y1, dx, dy), 2)

            elif mode == 'circle':
                radius_draw = int(math.hypot(dx, dy))
                pygame.draw.circle(screen, color, start_pos, radius_draw, 2)

            elif mode == 'square':
                side = min(abs(dx), abs(dy))
                square_rect = pygame.Rect(x1, y1, side if dx >= 0 else -side, side if dy >= 0 else -side)
                pygame.draw.rect(screen, color, square_rect, 2)

            elif mode == 'right_triangle':
                points = [start_pos, (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, points, 2)

            elif mode == 'equilateral_triangle':
                side = math.hypot(dx, dy)
                height = side * (math.sqrt(3) / 2)
                direction = -1 if dy < 0 else 1
                top_point = (x1 + dx / 2, y1 + direction * height)
                points = [start_pos, end_pos, top_point]
                pygame.draw.polygon(screen, color, points, 2)

            elif mode == 'rhombus':
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                points = [
                    (center_x, y1),      # Top
                    (x2, center_y),      # Right
                    (center_x, y2),      # Bottom
                    (x1, center_y)       # Left
                ]
                pygame.draw.polygon(screen, color, points, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
