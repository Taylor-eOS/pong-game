import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Ball properties
ball_image = pygame.image.load('ball.png')
ball_radius = ball_image.get_width() // 2
ball_pos = [(width // 2) - (width // 3), (height // 2) - (height // 3)]
ball_speed = [3, 3]

# Paddle properties
paddle_width = 100
paddle_height = 10
paddle_color = black
paddle_pos = [width // 2 - paddle_width // 2, height - 50]
paddle_speed = 10

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < width - paddle_width:
        paddle_pos[0] += paddle_speed

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off the walls
    if ball_pos[0] <= ball_radius or ball_pos[0] >= width - ball_radius:
        ball_speed[0] = -ball_speed[0]
        score += 1
    if ball_pos[1] <= ball_radius:
        ball_speed[1] = -ball_speed[1]
        score += 1

    # Increase speed every 10 points
    if score % 5 == 0 and score != 0:
        if ball_speed[0] > 0:
            ball_speed[0] += 1
        else:
            ball_speed[0] -= 1
        if ball_speed[1] > 0:
            ball_speed[1] += 1
        else:
            ball_speed[1] -= 1
        score += 1  # Temporarily increment score to avoid repeated speed increase

    # Bounce off the paddle
    if (paddle_pos[1] - ball_radius <= ball_pos[1] <= paddle_pos[1]) and (paddle_pos[0] <= ball_pos[0] <= paddle_pos[0] + paddle_width):
        ball_speed[1] = -ball_speed[1]

    # Check if ball hits the bottom
    if ball_pos[1] >= height - ball_radius:
        pygame.quit()
        sys.exit()

    # Clear screen
    window.fill(white)

    # Draw the ball
    window.blit(ball_image, (ball_pos[0] - ball_radius, ball_pos[1] - ball_radius))

    # Draw the paddle
    pygame.draw.rect(window, paddle_color, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))

    # Draw the score
    score_text = font.render(f'Score: {score}', True, black)
    window.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(50)
