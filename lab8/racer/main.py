import pygame
import random
import os

#Working directory
os.chdir(r"C:\Users\Bekzat\Documents\PP2\lab8\racer")

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Obstacles and Coins")

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
GREEN = (0, 150, 0)

car_img = pygame.image.load("car.png").convert_alpha()
coin_img = pygame.image.load("coin.png").convert_alpha()

car_img = pygame.transform.scale(car_img, (50, 100))
coin_img = pygame.transform.scale(coin_img, (30, 30))

player_rect = car_img.get_rect(center=(WIDTH // 2, HEIGHT - 120))
player_speed = 7

coin_rect = coin_img.get_rect(center=(random.randint(100, WIDTH - 100), -30))
coin_speed = 5
coins_collected = 0

enemy_img = pygame.transform.scale(car_img, (50, 100))  
obstacles = []
obstacle_spawn_rate = 90  
obstacle_timer = 0
obstacle_speed = 7
cars_avoided = 0

font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    clock.tick(FPS)
    obstacle_timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 100:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH - 100:
        player_rect.x += player_speed

    coin_rect.y += coin_speed
    if coin_rect.top > HEIGHT:
        coin_rect.center = (random.randint(100, WIDTH - 100), -30)

    if player_rect.colliderect(coin_rect):
        coins_collected += 1
        coin_rect.center = (random.randint(100, WIDTH - 100), -30)

    if obstacle_timer >= obstacle_spawn_rate:
        lane_x = random.choice([150, 250, 350, 450, 550])
        new_obstacle = enemy_img.get_rect(center=(lane_x, -100))
        obstacles.append(new_obstacle)
        obstacle_timer = 0

    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.top > HEIGHT:
            obstacles.remove(obstacle)
            cars_avoided += 1
        if player_rect.colliderect(obstacle):
            running = False   

    screen.fill(GREEN)
    pygame.draw.rect(screen, GRAY, (100, 0, WIDTH - 200, HEIGHT))

    screen.blit(car_img, player_rect)
    screen.blit(coin_img, coin_rect)

    for obs in obstacles:
        screen.blit(enemy_img, obs)

    coin_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    avoided_text = font.render(f"Avoided: {cars_avoided}", True, WHITE)
    screen.blit(coin_text, (WIDTH - 150, 10))
    screen.blit(avoided_text, (WIDTH - 150, 40))

    pygame.display.flip()

pygame.quit()
