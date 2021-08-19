import time
import pygame
from point import point
from firework import firework

pygame.init()
num_points = 20
fps = 0.05

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
step = 0
#points = [point(250, 500)]
explosion_center = None
firework_one = firework(startingX=250, startingY=500, num_points=10, color=(0,0,255), height=100, width=50, maxSparksize=5)
firework_two = firework(startingX=150, startingY=500, num_points=10, color=(255,0,0), height=100, width=30, maxSparksize=10)
firework_three = firework(startingX=350, startingY=500, num_points=10, color=(0,255,0), height=200, width=30, maxSparksize=10)

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    step = step + 1
    i = 0
    time.sleep(fps)
    #firework_one.updateStep()


    # Fill the background with white
    screen.fill((255, 255, 255))

    firework_one.updateStep()
    firework_one.drawShoot(pygame, screen)

    #firework_two.updateStep()
    #firework_two.drawShoot(pygame, screen)

    #firework_three.updateStep()
    #firework_three.drawShoot(pygame, screen)
    # if (step == 100):
    #     explosion_center = point(points[0].x, points[0].y)
    #     for i in range(0, num_points):
    #         points = points + [point(explosion_center.x, explosion_center.y)]
    #
    # while i < len(points):
    #     if (step < 100):
    #         if points[i].y > 0:
    #             points[i].y = points[i].y - 1
    #
    #     if (step > 100 and step < 200):
    #         #points[i].x = points[i].x + i
    #         points[i].y = explosion_center.y + math.sin(2*(i / num_points)*2*math.pi) * (step - 100) * 0.5
    #         points[i].x = explosion_center.x + math.cos(2*(i / num_points)*2*math.pi) * (step - 100) * 0.5
    #
    #     #pygame.draw.circle(screen, (0, 0, 255.0 * i / len(points)), (points[i].x, points[i].y), 10)
    #     i = i + 1

    # Draw a solid blue circle in the center
    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()