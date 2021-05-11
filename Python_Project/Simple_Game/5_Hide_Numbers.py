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

    cell_size = 130
    button_size = 110  # actual button size include margin
    screen_leftmargin = 55  # left margin
    screen_topmargin = 20  # top margin

    grid = [[0 for col in range(columns)] for row in range(rows)]  # 5 x 9

    number = 1  # Start number from 1 to number_count
    while number <= number_count:
        row_idx = randrange(0, rows)  # 0, 1, 2, 3, 4
        col_idx = randrange(0, columns)  # 0, 1, 2 ... 8

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number  # Select number
            number += 1

            # calculate X and Y
            center_x = screen_leftmargin + \
                (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_topmargin + \
                (row_idx * cell_size) + (cell_size / 2)

            # create number button
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    print(grid)  # Check random number


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


def display_game_screen():
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            # draw button
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # add number text
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)


def check_buttons(pos):
    global start

    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True


def check_number_buttons(pos):
    global hidden

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print("wrong")
            break


# Basic Frame
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120)  # define font

# Start Button
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

number_buttons = []  # playing button

# Start
start = False
# hidden numbers
hidden = False

# game setting
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
