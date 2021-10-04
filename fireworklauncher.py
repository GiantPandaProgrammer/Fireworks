import time
import pygame
from firework import firework

pygame.init()
num_points = 20
fps = 0.01

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
step = 0

explosion_center = None


fireworks = []
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            firework_one = firework(startingX=pos[0], startingY=pos[1], num_points=10, color=(255, 255, 255), height=100,
                                    width=200,
                                    maxSparksize=20)
            fireworks = fireworks + [firework_one]

    fireworks = filter(lambda firework: not firework.isDone(), fireworks)
    step = step + 1
    i = 0
    time.sleep(fps)

    # Fill the background with white
    screen.fill((255, 255, 255))

    for fw in fireworks:
        fw.updateStep()
        fw.drawShoot(pygame, screen)

    #firework_two.updateStep()
    #firework_two.drawShoot(pygame, screen)

    #firework_three.updateStep()
    #firework_three.drawShoot(pygame, screen)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()