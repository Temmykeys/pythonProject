
import pygame


pygame.init()

PURPLE = (188, 81, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 240)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653
size = (700, 500)
screen = pygame.display.set_mode(size)

button_colour = BLACK
# defines how button is drawn
def button(x_pos, y_pos, text):
    pygame.draw.rect(screen, BLUE, [x_pos, y_pos, 250, 40])
    button_font = pygame.font.SysFont('Calibri', 40, True, False)
    button = button_font.render(text, True, button_colour)
    screen.blit(button, [x_pos + 10, y_pos + 3])

pygame.display.set_caption("Coomputer programming")

# Loops until close button is clicked.
done = False
clock = pygame.time.Clock()
while not done:
    def button_pressed():
        x, y = pygame.mouse.get_pos()
        print(x, y)


    button_pressed()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
    # background colour
    screen.fill(GREEN)
    # main menu button
    button(220, 90, 'Main menu')
    # settings button
    button(220, 240, 'Settings')
    # Help button
    button(220, 390, 'Help')
    # Draws base rectangle
    pygame.draw.rect(screen, BLACK, [0, size[1]-20, size[0], 20])
    pygame.display.flip()

    clock.tick(90)

pygame.quit()