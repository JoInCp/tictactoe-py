import pygame 

WHITE = (255, 255, 255)
RECT_SIZE = 150
BLANK_SIZE = 25

pygame.init()

window = pygame.display.set_mode((550, 550))

pygame.display.set_caption('Tic-Tac-Toe')

matrix = [[[pygame.draw.rect(window, WHITE, (BLANK_SIZE * (col + 1) + RECT_SIZE * col, BLANK_SIZE * (row + 1) + RECT_SIZE * row, RECT_SIZE, RECT_SIZE)), -1] for col in  range(3)] for row in range(3)]

run = True

while run:
  pygame.time.delay(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()