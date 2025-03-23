import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Extended Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color = BLACK  
radius = 5

mode = 'draw'  

start_pos = None

screen.fill(WHITE)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE
            
            elif event.key == pygame.K_d:
                mode = 'draw'
            elif event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_e:
                mode = 'erase'

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
            if mode == 'rect' and start_pos:
                x, y = start_pos
                w, h = end_pos[0] - x, end_pos[1] - y
                pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h), 2)
            elif mode == 'circle' and start_pos:
                x, y = start_pos
                radius_draw = int(((end_pos[0] - x) ** 2 + (end_pos[1] - y) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius_draw, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()