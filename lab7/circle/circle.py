import pygame
import sys

pygame.init()

# Screen setup
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Red Ball")

# Ball properties
radius = 25
x, y = width // 2, height // 2
speed = 20

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y + radius + speed <= height:
                y += speed
            elif event.key == pygame.K_LEFT and x - radius - speed >= 0:
                x -= speed
            elif event.key == pygame.K_RIGHT and x + radius + speed <= width:
                x += speed

    # Draw background
    screen.fill((255, 255, 255))

    # Draw red ball
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
