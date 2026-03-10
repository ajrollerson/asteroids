import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *
import constants
from soundeffects import pew_sound

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.player_shoot_cooldown = 0
        self.velocity = pygame.Vector2(0, 0)
        self.player_shoot_cooldown_base = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        self.player_shoot_cooldown = 0
        self.player_shot_speed = constants.PLAYER_SHOOT_SPEED

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_ROTATION_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector    
    
    def update(self, dt):
        self.player_shoot_cooldown -= dt
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 2).rotate(self.rotation)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.velocity -= forward * PLAYER_ACCELERATION * dt
            if self.velocity.length() > PLAYER_MAX_SPEED:
                self.velocity.scale_to_length(PLAYER_MAX_SPEED)
        if keys[pygame.K_w]:
            self.velocity += forward * PLAYER_ACCELERATION * dt
            if self.velocity.length() > PLAYER_MAX_SPEED:
                self.velocity.scale_to_length(PLAYER_MAX_SPEED)

        self.position += self.velocity * dt
        self.velocity -= self.velocity * DAMPENING_FACTOR * dt


        if keys[pygame.K_SPACE]:
            if self.player_shoot_cooldown > 0:
                return
            self.player_shoot_cooldown = self.player_shoot_cooldown_base
            self.shoot()


    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        bullet.position = self.position + forward * self.radius
        pew_sound.play()
    