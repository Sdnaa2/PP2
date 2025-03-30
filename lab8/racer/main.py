import pygame
import random
import os

# Set working directory to access images
os.chdir(r"C:\Users\Bekzat\Documents\PP2\lab8\racer")

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Obstacles and Coins")

# Define colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
GREEN = (0, 150, 0)

# Load car and coin images
car_img = pygame.image.load("car.png").convert_alpha()
coin_img_original = pygame.image.load("coin.png").convert_alpha()

# Resize car image
car_img = pygame.transform.scale(car_img, (50, 100))

# Set up player (car) properties
player_rect = car_img.get_rect(center=(WIDTH // 2, HEIGHT - 120))
player_speed = 7

# --- Updated Part: Setup for coins with different weights (sizes) ---
# Function to spawn a coin with random size (weight)
def spawn_coin():
    scale = random.randint(20, 50)  # Random size from 20 to 50 pixels
    coin_img = pygame.transform.scale(coin_img_original, (scale, scale))  # Resize coin image
    coin_rect = coin_img.get_rect(center=(random.randint(100, WIDTH - 100), -scale))  # Random X position
    return coin_img, coin_rect

# Spawn the initial coin
coin_img, coin_rect = spawn_coin()
coin_speed = 5
coins_collected = 0
# --- End of updated part ---

# Set up obstacles (enemy cars)
enemy_img = pygame.transform.scale(car_img, (50, 100))  
obstacles = []
obstacle_spawn_rate = 90  # Frames between each obstacle spawn
obstacle_timer = 0
obstacle_speed = 7
cars_avoided = 0

# Font for UI text
font = pygame.font.SysFont("Arial", 30)

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

# Game loop
running = True
while running:
    clock.tick(FPS)
    obstacle_timer += 1

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 100:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH - 100:
        player_rect.x += player_speed

    # Move coin downward
    coin_rect.y += coin_speed
    if coin_rect.top > HEIGHT:
        coin_img, coin_rect = spawn_coin()  # Respawn coin if it goes off screen

    # Check collision between player and coin
    if player_rect.colliderect(coin_rect):
        coins_collected += 1
        coin_img, coin_rect = spawn_coin()  # Respawn coin after collection

    # Spawn new obstacle car periodically
    if obstacle_timer >= obstacle_spawn_rate:
        lane_x = random.choice([150, 250, 350, 450, 550])  # Random lane position
        new_obstacle = enemy_img.get_rect(center=(lane_x, -100))
        obstacles.append(new_obstacle)
        obstacle_timer = 0

    # Move obstacles and check collisions
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.top > HEIGHT:
            obstacles.remove(obstacle)
            cars_avoided += 1
        if player_rect.colliderect(obstacle):
            running = False  # End game on collision

    # Draw background
    screen.fill(GREEN)
    pygame.draw.rect(screen, GRAY, (100, 0, WIDTH - 200, HEIGHT))  # Road

    # Draw player car and coin
    screen.blit(car_img, player_rect)
    screen.blit(coin_img, coin_rect)

    # Draw obstacles
    for obs in obstacles:
        screen.blit(enemy_img, obs)

    # Draw UI text
    coin_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    avoided_text = font.render(f"Avoided: {cars_avoided}", True, WHITE)
    screen.blit(coin_text, (WIDTH - 150, 10))
    screen.blit(avoided_text, (WIDTH - 150, 40))

    # Update display
    pygame.display.flip()

# Quit game
pygame.quit()
