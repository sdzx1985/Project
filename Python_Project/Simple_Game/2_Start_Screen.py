import pygame


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


# Basic Frame
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# Start Button
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game Loop
running = True
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # End game

    # Background Color
    screen.fill(BLACK)

    # Start screen
    display_start_screen()

    # Screen update
    pygame.display.update()

# End game
pygame.quit()
