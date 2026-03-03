from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = uniform(20,50)
        new_ast_1_vel = self.velocity.rotate(angle)
        new_ast_2_vel = self.velocity.rotate(-angle)
        new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position[0], self.position[1], new_ast_radius)
        new_ast_2 = Asteroid(self.position[0], self.position[1], new_ast_radius)
        new_ast_1.velocity = new_ast_1_vel * 1.2
        new_ast_2.velocity = new_ast_2_vel * 1.2
