import pygame
from random import *


def setup(level):  # Level setting
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)  # Maximum number = 20

    # Actual screen
    shuffle_grid(number_count)


def shuffle_grid(number_count):  # Shuffle number
    rows = 5
    columns = 9

    grid = [[0 for col in range(columns)] for row in range(rows)]  # 5 x 9

    number = 1  # Start number from 1 to number_count
    while number <= number_count:
        row_idx = randrange(0, rows)  # 0, 1, 2, 3, 4
        col_idx = randrange(0, columns)  # 0, 1, 2 ... 8

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number  # Select number
            number += 1

    print(grid)  # Check random number


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


def display_game_screen():
    # print("Game Start")
    pass


def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True


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

# Start
start = False

setup(1)

# Game Loop
running = True
while running:
    click_pos = None

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # End game
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            # print(click_pos)

    # Background Color
    screen.fill(BLACK)

    if start:
        display_game_screen()  # Game screen
    else:
        display_start_screen()  # Start screen

    # User click
    if click_pos:
        check_buttons(click_pos)

    # Screen update
    pygame.display.update()

# End game
pygame.quit()
