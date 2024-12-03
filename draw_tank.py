import math
import pygame

# Draw tank
def draw_tank(surface, position, angle, size, color):
  tank_points = [
    (position[0] + size * math.cos(math.radians(angle)),
      position[1] - size * math.sin(math.radians(angle))),
    (position[0] + size * math.cos(math.radians(angle + 120)),
      position[1] - size * math.sin(math.radians(angle + 120))),
    (position[0] + size * math.cos(math.radians(angle + 240)),
      position[1] - size * math.sin(math.radians(angle + 240)))
  ]
  pygame.draw.polygon(surface, color, tank_points)