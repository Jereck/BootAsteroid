import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    rand_ang = random.uniform(20, 50)

    a = self.velocity.rotate(rand_ang)
    b = self.velocity.rotate(-rand_ang)

    new_rad = self.radius - ASTEROID_MIN_RADIUS
    asteroid = Asteroid(self.position.x, self.position.y, new_rad)
    asteroid.velocity = a * 1.2
    asteroid = Asteroid(self.position.x, self.position.y, new_rad)
    asteroid.velocity = b * 1.2