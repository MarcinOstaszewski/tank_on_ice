import pygame
from draw_tank import draw_tank
from check_keyboard import check_keyboard
from constants import WIDTH, HEIGHT

# Initialize pygame
pygame.init()

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define tank properties
tank = {
    "size": 13,
    "pos": [WIDTH // 2, HEIGHT // 2],
    "angle": 90,
    "velocity": 0,
    "vertical_speed": 0,
    "horizontal_speed": 0,
    "rotation_speed": 0
}

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Check keyboard input and update tank properties
  tank = check_keyboard(tank)

  # Update display
  window.fill(black)
  # Call the function to draw the tank
  draw_tank(window, tank["pos"], tank["angle"], tank["size"], white)
  pygame.display.flip()

  # Cap the frame rate
  clock.tick(60)

pygame.quit()