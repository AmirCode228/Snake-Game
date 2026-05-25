import pygame
import random
import sys

WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

snake = [(200, 200), (180, 200), (160, 200)]

DIRECTION = 'RIGHT'

food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
        random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

score = 0

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

def show_score(score):
    font = pygame.font.SysFont(None, 35)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and DIRECTION != 'DOWN':
                DIRECTION = 'UP'
            elif event.key == pygame.K_s and DIRECTION != 'UP':
                DIRECTION = 'DOWN'
            elif event.key == pygame.K_a and DIRECTION != 'RIGHT':
                DIRECTION = 'LEFT'
            elif event.key == pygame.K_d and DIRECTION != 'LEFT':
                DIRECTION = 'RIGHT'

    head_x, head_y = snake[0]
    if DIRECTION == 'UP':
        head_y -= BLOCK_SIZE
    elif DIRECTION == 'DOWN':
        head_y += BLOCK_SIZE
    elif DIRECTION == 'LEFT':
        head_x -= BLOCK_SIZE
    elif DIRECTION == 'RIGHT':
        head_x += BLOCK_SIZE

    if (head_x <= 0 or head_x >= WIDTH or
        head_y <= 0 or head_y >= HEIGHT):
        game_over = True

    new_head = (head_x, head_y)
    if new_head in snake:
        game_over = True
    
    snake.insert(0, new_head)

    if snake[0] == food:
        score += 1

        while True:
            new_food = (
                random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            )
            if new_food not in snake:
                food = new_food
                break
    else:
        snake.pop()
    
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    show_score(score)

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit
sys.exit()