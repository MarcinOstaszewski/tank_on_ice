import pygame
import math
from constants import MAX_SPEED, MAX_ROTATION_SPEED, ACCELERATION, DECELERATION, ROTATION_ACCELERATION, ROTATION_DECELERATION, WIDTH, HEIGHT

def check_keyboard(tank):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        tank['velocity'] = min(tank['velocity'] + ACCELERATION, MAX_SPEED)
        tank['horizontal_speed'] += ACCELERATION * math.cos(math.radians(tank['angle']))
        tank['vertical_speed'] -= ACCELERATION * math.sin(math.radians(tank['angle']))
    else:
        tank['horizontal_speed'] *= DECELERATION
        tank['vertical_speed'] *= DECELERATION

    if keys[pygame.K_DOWN]:
        tank['velocity'] = max(tank['velocity'] - ACCELERATION, -MAX_SPEED)
        tank['horizontal_speed'] -= ACCELERATION * math.cos(math.radians(tank['angle']))
        tank['vertical_speed'] += ACCELERATION * math.sin(math.radians(tank['angle']))
    if keys[pygame.K_LEFT]:
        if tank['rotation_speed'] < MAX_ROTATION_SPEED:
            tank['rotation_speed'] += ROTATION_ACCELERATION
    if keys[pygame.K_RIGHT]:
        if tank['rotation_speed'] > -MAX_ROTATION_SPEED:
            tank['rotation_speed'] -= ROTATION_ACCELERATION

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        tank['rotation_speed'] *= ROTATION_DECELERATION

    # Update tank angle
    tank['angle'] += tank['rotation_speed']

    # Update tank position with boundary check
    new_x = tank["pos"][0] + tank["horizontal_speed"]
    new_y = tank["pos"][1] + tank["vertical_speed"]
    if tank["size"] <= new_x <= WIDTH - tank["size"]:
      tank["pos"][0] = new_x
    if tank["size"] <= new_y <= HEIGHT - tank["size"]:
      tank["pos"][1] = new_y

    return tank