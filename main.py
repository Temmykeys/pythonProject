
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

pygame.display.set_caption("Computing Project")

# Loops until close button is clicked.
done = False
clock = pygame.time.Clock()
screen.fill(GREEN)
while not done:
    def button_pressed():
        x, y = pygame.mouse.get_pos()

        def draw_button(x_pos, y_pos, text):
            if x_pos < x < x_pos+250 and y_pos < y < y_pos + 40:
                button_colour = PURPLE
                text_colour = BLACK

            else:
                button_colour = BLUE
                text_colour = BLACK

            pygame.draw.rect(screen, button_colour, [x_pos, y_pos, 250, 40])
            button_font = pygame.font.SysFont('Calibri', 40, True, False)
            button_text = button_font.render(text, True, text_colour)

            screen.blit(button_text, [x_pos + 10, y_pos + 3])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and button_colour == PURPLE:
                    print('button clicked')
                    draw_button(220, 90, 'Classic mode')
        draw_button(220, 390, 'Help')
        draw_button(220, 240, 'Settings')
        draw_button(220, 90, 'Main menu')
    button_pressed()
    # draws base rectangle
    pygame.draw.rect(screen, BLACK, [0, size[1] - 20, size[0], 20])

    clock.tick(90)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicks close
            done = True

pygame.quit()
