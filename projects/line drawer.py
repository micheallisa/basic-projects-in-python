import pygame

# Defines the color variables for the program
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TEXTCOLOR = (0, 0, 0)
(width, height) = (int(input("Please enter the width of your window: ")), int(input("Please enter the height of your window: ")))


pygame.init()

# Set the display size to the one inputted by the user, and opens the display.
dis = pygame.display.set_mode((width, height))
pygame.display.update()
dis.fill(RED)
pygame.display.set_caption('bird game by micheallisa')
game_over = False

# Gets the position of the mouse


def get_pos():
    pos = pygame.mouse.get_pos()
    return pos

# Draws a line


def draw_line():
    pos = get_pos()
    pygame.draw.line(dis, YELLOW, pos, pos, 100)

# makes it so that the window doesn't instantly close and draws the lines.
while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        draw_line()
        pygame.display.update()


