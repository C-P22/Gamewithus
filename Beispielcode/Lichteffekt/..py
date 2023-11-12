import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WINDOW_SIZE = (800, 600)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main game loop
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Moving Light Effect Example")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the moving light source
    pygame.draw.circle(screen, WHITE, mouse_pos, 50)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
