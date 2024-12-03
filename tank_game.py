import pygame
import math
from draw_tank import draw_tank
from check_keyboard import check_keyboard

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tank Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define tank properties
tank_size = 13
tank_pos = [width // 2, height // 2]
tank_angle = 90
tank_velocity = 0
tank_vertical_speed = 0
tank_horizontal_speed = 0
tank_rotation_speed = 0
max_speed = 6
max_rotation_speed = 5
acceleration = 0.15
deceleration = 0.98
rotation_acceleration = 0.2
rotation_deceleration = 0.95

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Check keyboard input and update tank properties
  tank_velocity, tank_horizontal_speed, tank_vertical_speed, tank_rotation_speed, tank_angle = check_keyboard(
    tank_velocity, tank_horizontal_speed, tank_vertical_speed, tank_rotation_speed, tank_angle, acceleration, deceleration, rotation_acceleration, rotation_deceleration, max_speed, max_rotation_speed
  )

  # Update tank position with boundary check
  new_x = tank_pos[0] + tank_horizontal_speed
  new_y = tank_pos[1] + tank_vertical_speed
  if tank_size <= new_x <= width - tank_size:
    tank_pos[0] = new_x
  if tank_size <= new_y <= height - tank_size:
    tank_pos[1] = new_y

  # Clear screen
  window.fill(black)

  # Call the function to draw the tank
  draw_tank(window, tank_pos, tank_angle, tank_size, white)

  # Update display
  pygame.display.flip()

  # Cap the frame rate
  clock.tick(60)

pygame.quit()