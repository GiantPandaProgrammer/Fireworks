from point import point;
import math
from random import randint
# Click on shoot up fireworks
# What happened to the stem ?


# Random color Red Green Blue
# Gradient of color from light to bright to light
# Size from small to big back to small
    # Sin function Sin ( pi * 0 => 1)
    # black to blue => white to blue ?
    # use cos for r and b and keep g at 255

class firework():
    step = 0
    initialSparkSize = 5

    # one to many
    def __init__(self, startingX, startingY, num_points, color, height, width, maxSparksize):
        self.sparks = [point(startingX, startingY)]
        self.num_points = num_points
        self.color = color
        self.height = height
        self.width = width
        self.maxSize = maxSparksize
        self.currentSize = self.initialSparkSize
        self.sinpercent = 0
        self.cospercent = 1
        self.startingX = startingX
        self.startingY = startingY

        self.reinitialize()

    def updateStep(self):
        self.step = self.step + 1
        for i in range(0, len(self.sparks)):
            if (self.step < self.height):
                self.sparks[i].y = self.sparks[i].y - 1
            if (self.step == self.height):
                self.explosionCenter = point(self.sparks[0].x, self.sparks[0].y)
                for i in range(0, self.num_points):
                    self.sparks = self.sparks + [point(self.sparks[0].x, self.sparks[0].y)]

            if (self.height <= self.step and self.step <= self.height + self.width):
                explodeStep = self.step - self.height
                self.sinpercent = (math.sin(float(explodeStep) / self.width * math.pi))
                self.cospercent = (math.cos(float(explodeStep) / self.width * 2 * math.pi) + 1) / 2
                #if (self.cospercent > 1):
                #    self.cospercent = 1
                #if (self.cospercent < 0):
                #    self.cospercent = 0

                self.currentSize = self.initialSparkSize + self.sinpercent * self.maxSize

                self.sparks[i].y = self.explosionCenter.y + math.sin((i / float(self.num_points)) * 2 * math.pi) * (self.step - self.height)
                self.sparks[i].x = self.explosionCenter.x + math.cos((i / float(self.num_points)) * 2 * math.pi) * (self.step - self.height)

    def isDone(self):
        return self.step > self.height + self.width

    def reinitialize(self):
        self.currentSize = 0
        self.step = 0
        self.sparks = [point(self.startingX, self.startingY)]
        self.currentSize = self.initialSparkSize
        self.rgb = randint(0, 2)


    def drawShoot(self, py, screen):
        if self.isDone():
            return

        for i in range(0, len(self.sparks)):
            color = (0, 0, 0)
            currentColorStep = self.step - self.height
            if currentColorStep > 0 and currentColorStep <= self.width:

                if self.rgb == 0:
                    color = (255 * self.cospercent, 255, 255 * self.cospercent)
                elif self.rgb == 1:
                    color = (255, 255 * self.cospercent, 255 * self.cospercent)
                else:
                    color = (255 * self.cospercent, 255 * self.cospercent, 255)

            py.draw.circle(screen, color, (self.sparks[i].x, self.sparks[i].y), self.currentSize)