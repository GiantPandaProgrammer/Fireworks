from point import point;
import math

class firework():
    step = 0
    #explosionCenter = point(0,0)

    # one to many
    def __init__(self, startingX, startingY, num_points, color, height, width, sparksize):
        self.sparks = [point(startingX, startingY)]
        self.num_points = num_points
        self.color = color
        self.height = height
        self.width = width
        self.sparksize = sparksize

    def updateStep(self):
        self.step = self.step + 1
        for i in range(0, len(self.sparks)):
            if (self.step < self.height):
                self.sparks[i].y = self.sparks[i].y - 1
            if (self.step == self.height):
                self.explosionCenter = point(self.sparks[0].x, self.sparks[0].y)
                for i in range(0, self.num_points):
                    self.sparks = self.sparks + [point(self.sparks[0].x, self.sparks[0].y)]

            if (self.step > self.height and self.step < self.height + self.width):
                math.sin((i / float(self.num_points)) * 2 * math.pi)
                self.sparks[i].y = self.explosionCenter.y + math.sin((i / float(self.num_points)) * 2 * math.pi) * (self.step - self.height)
                self.sparks[i].x = self.explosionCenter.x + math.cos((i / float(self.num_points)) * 2 * math.pi) * (self.step - self.height)

    def drawShoot(self, py, screen):
        for i in range(0, len(self.sparks)):

            color = self.color
            color_range = self.width
            currentColorStep = self.step - self.height
            percentSize = 1
            if currentColorStep > 0 and currentColorStep < self.width:
                percentSize = float(currentColorStep) / self.width

            #Parabolic function?
            sparksize = self.sparksize

            py.draw.circle(screen, self.color, (self.sparks[i].x, self.sparks[i].y), sparksize * percentSize)