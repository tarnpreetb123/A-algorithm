import os
import pygame
import Grid

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Windoweva
window_size = (1200, 700)
gameDisplay = pygame.display.set_mode(window_size)
pygame.display.set_caption('A* Algorithm')

# Frame rate and clock
clock = pygame.time.Clock()
running = True
solving = False

# Create a new grid
grid = Grid.Grid(gameDisplay)

# Game Loop
while running:
    deltaT = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_q]:

            solving = True

    gameDisplay.fill(gray)

    # Update and draw the grid only if the openSet is not empty and if solving has began
    if grid.openSetNotEmpty() and solving:
        grid.update()
    # Otherwise let the user draw in walls
    else:
        grid.update_mouse()

        if key[pygame.K_w]:
            grid.reset()

            solving = False

    grid.draw()

    pygame.display.flip()

pygame.quit()