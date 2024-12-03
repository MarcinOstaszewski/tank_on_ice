
import pygame
import math

def check_keyboard(tank_velocity, tank_horizontal_speed, tank_vertical_speed, tank_rotation_speed, tank_angle, acceleration, deceleration, rotation_acceleration, rotation_deceleration, max_speed, max_rotation_speed):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    tank_velocity = min(tank_velocity + acceleration, max_speed)
    tank_horizontal_speed += acceleration * math.cos(math.radians(tank_angle))
    tank_vertical_speed -= acceleration * math.sin(math.radians(tank_angle))
  else:
    tank_horizontal_speed *= deceleration
    tank_vertical_speed *= deceleration

  if keys[pygame.K_DOWN]:
    tank_velocity = max(tank_velocity - acceleration, -max_speed)
    tank_horizontal_speed -= acceleration * math.cos(math.radians(tank_angle))
    tank_vertical_speed += acceleration * math.sin(math.radians(tank_angle))
  if keys[pygame.K_LEFT]:
    if tank_rotation_speed < max_rotation_speed:
      tank_rotation_speed += rotation_acceleration
  if keys[pygame.K_RIGHT]:
    if tank_rotation_speed > -max_rotation_speed:
      tank_rotation_speed -= rotation_acceleration

  if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
    tank_rotation_speed *= rotation_deceleration

  # Update tank angle
  tank_angle += tank_rotation_speed

  return tank_velocity, tank_horizontal_speed, tank_vertical_speed, tank_rotation_speed, tank_angle