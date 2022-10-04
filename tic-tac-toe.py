import pygame 

pygame.init()

window = pygame.display.set_mode((550, 550))

pygame.display.set_caption('Tic-Tac-Toe')

run = True

while run:
  pygame.time.delay(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()