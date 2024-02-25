import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
screen_width = 600
screen_height = 400
block_size = 20  # Size of snake and food blocks
speed = 10  # Starting game speed

# Colors for the game
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)  # Snake
red = (255, 0, 0)  # Food

# Fonts
font = pygame.font.SysFont(None, 30)

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Classic Snake Game")

# Control the game speed
clock = pygame.time.Clock()


def draw_snake(snake_list):
    """Draws the snake on the screen."""
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])


def display_score(score):
    """Displays the current score"""
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, (10, 10))


def game_loop():
    """The main game loop."""
    game_over = False
    game_close = False

    # Starting positions
    x = screen_width / 2
    y = screen_height / 2
    x_change = 0
    y_change = 0

    # Snake body as a list
    snake_list = []
    snake_length = 1

    # Generate random food location
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    while not game_over:

        # "Game Close" screen - Player can quit or restart
        while game_close:
            screen.fill(black)
            msg = font.render("Game Over! Press Q (Quit) or R (Restart)", True, white)
            screen.blit(msg, (screen_width / 6, screen_height / 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()  # Restart

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Boundary check & game over
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True

            # Update snake position
        x += x_change
        y += y_change
        screen.fill(black)

        # Draw food
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        # ... [See next code block for explanation] ...
        # Snake body mechanics
        snake_head = [x,y]
        snake_list.append(snake_head)

        # Limit snake length based on score
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Detect if snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Eating food mechanic
        if x == food_x and y == food_y:
            # New food location
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(speed)  # Control the speed

    pygame.quit()
    quit()

# Start the game
game_loop()
