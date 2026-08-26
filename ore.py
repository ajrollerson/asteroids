import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH

class Ore(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.ore_type = random.choice(["purple_ore", "red_ore", "blue_ore", "green_ore"])
        if self.ore_type == "purple_ore":
            self.colour = ("purple")
        if self.ore_type == "red_ore":
            self.colour = ("red")
        if self.ore_type == "blue_ore":
            self.colour = ("blue")
        if self.ore_type == "green_ore":
            self.colour = ("green")

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
