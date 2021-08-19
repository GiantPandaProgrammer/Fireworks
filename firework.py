from point import point;
import math


# Gradient of color from light to bright to light
# Size from small to big back to small
# Click on shoot up fireworks
# Random color Red Green Blue
# Sin function Sin ( pi * 0 => 1)


class firework():
    step = 0
    initialSparkSize = 1

    # one to many
    def __init__(self, startingX, startingY, num_points, color, height, width, maxSparksize):
        self.sparks = [point(startingX, startingY)]
        self.num_points = num_points
        self.color = color
        self.height = height
        self.width = width
        self.maxSize = maxSparksize
        self.currentSize = self.initialSparkSize

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
                self.currentSize = self.initialSparkSize + math.sin(float(explodeStep) / self.width * math.pi) * self.maxSize

                self.sparks[i].y = self.explosionCenter.y + math.sin((i / float(self.num_points)) * 2 * math.pi) * (self.step - self.height)
                self.sparks[i].x = self.explosionCenter.x + math.cos((i / float(self.num_points)) * 2 * math.pi) * (self.step - self.height)

            if (self.step > self.height + self.width):
                self.currentSize = 0

    def drawShoot(self, py, screen):
        for i in range(0, len(self.sparks)):
            color = self.color
            color_range = self.width
            currentColorStep = self.step - self.height
            percentSize = 1
            if currentColorStep > 0 and currentColorStep < self.width:
                percentSize = float(currentColorStep) / self.width

            py.draw.circle(screen, self.color, (self.sparks[i].x, self.sparks[i].y), self.currentSize)