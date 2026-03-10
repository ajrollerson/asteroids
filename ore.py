import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH

class Ore(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.ore_type = random.choice(["cool_crystal", "lasor_crystal", "score", "radioactive"])
        if self.ore_type == "cool_crystal":
            self.colour = ("purple")
        if self.ore_type == "lasor_crystal":
            self.colour = ("red")
        if self.ore_type == "score":
            self.colour = ("blue")
        if self.ore_type == "radioactive":
            self.colour = ("green")

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
