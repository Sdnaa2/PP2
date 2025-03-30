import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initial snake setup
snake = [(300, 200), (290, 200), (280, 200)]
snake_direction = 'RIGHT'
snake_speed = 10

# --- Updated Part: Random food size (weight) ---
def generate_food():
    while True:
        position = (random.randrange(0, width, 10), random.randrange(0, height, 10))
        if position not in snake:
            size = random.choice([10, 20, 30])  # Weight represented by food size
            return position, size
# --- End of updated part ---

food_position, food_size = generate_food()  # Initialize food

score = 0
level = 1
food_needed_for_next_level = 4

font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # Move the snake head
    head_x, head_y = snake[0]
    if snake_direction == 'RIGHT':
        head_x += 10
    elif snake_direction == 'LEFT':
        head_x -= 10
    elif snake_direction == 'UP':
        head_y -= 10
    elif snake_direction == 'DOWN':
        head_y += 10

    # Check for collisions with wall or itself
    if (head_x >= width or head_x < 0 or head_y >= height or head_y < 0 or (head_x, head_y) in snake):
        running = False

    snake.insert(0, (head_x, head_y))

    # Check for food collision
    fx, fy = food_position
    if fx <= head_x < fx + food_size and fy <= head_y < fy + food_size:
        score += 1

        # Grow the snake based on food weight (size // 10 units)
        for _ in range((food_size // 10) - 1):
            snake.insert(0, snake[0])  # Insert extra segments at head

        food_position, food_size = generate_food()  # Respawn new random food

        if score % food_needed_for_next_level == 0:
            level += 1
            snake_speed += 2
    else:
        snake.pop()

    # Draw game
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food with its weight (size)
    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], food_size, food_size))

    # Display score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()
