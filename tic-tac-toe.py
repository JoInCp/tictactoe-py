from multiprocessing import current_process
from tabnanny import check
import pygame 

WHITE = (255, 255, 255)
RED = (255, 0, 0)
WINDOW_SIZE = 550
RECT_SIZE = 150
CIRCLE_SIZE = 50
BLANK_SIZE = 25
LINE_SIZE = 3
STATUS = ['O', 'X', None]
TURNS = ['O', 'X']

pygame.init()

window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) #150 * 3 + 25 * 4

pygame.display.set_caption('Tic-Tac-Toe')

matrix = [[[pygame.draw.rect(window, WHITE, (BLANK_SIZE * (col + 1) + RECT_SIZE * col, BLANK_SIZE * (row + 1) + RECT_SIZE * row, RECT_SIZE, RECT_SIZE)), -1] for col in  range(3)] for row in range(3)]

# matrix = [] #정사각형 칸만들기
# for row in range(3):
#   for col in range(3):
#     rect = pygame.draw.rect(window, WHITE, (BLANK_SIZE * (col + 1) + RECT_SIZE * col, BLANK_SIZE * (row + 1) + RECT_SIZE * row, RECT_SIZE, RECT_SIZE))
#     status = -1
#     matrix.append([rect, status])

run = True
end_game = False
true_value = 0
current_turn = TURNS[true_value%2]

while run:
  pygame.time.delay(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


    if event.type == pygame.MOUSEBUTTONUP: #클릭처리 및 화면 O/X표시
      pos = pygame.mouse.get_pos()

      for row in  range(3):
        for col in range(3):
          if matrix[row][col][0].collidepoint(pos): 
            if STATUS [matrix[row][col][1]] is None:
              current_turn = TURNS[true_value%2]
              if current_turn == 'O':
                pygame.draw.circle(window, RED, matrix[row][col][0].center, CIRCLE_SIZE)
                matrix[row][col][1] = true_value%2

              elif current_turn == 'X':
                pygame.draw.line(window, RED, matrix[row][col][0].topleft, matrix[row][col][0].bottomright, LINE_SIZE)
                pygame.draw.line(window, RED, matrix[row][col][0].topright, matrix[row][col][0].bottomleft, LINE_SIZE)
                matrix[row][col][1] = true_value%2
              
              true_value += 1

              for _row in range(3): #가로확인
                check = 0
                for _col in range(3):
                  if STATUS[matrix[_row][_col][1]] == current_turn:
                    check += 1
                if check == 3:
                  end_game = True

              for _col in range(3): #세로확인
                check = 0
                for _row in range(3):
                  if STATUS[matrix[_row][_col][1]] == current_turn:
                    check += 1
                if check == 3:
                  end_game = True

              check = 0 #우대각확인
              for _col, _row in zip(range(3), range(3)):
                if STATUS[matrix[_row][_col][1]] == current_turn:
                  check += 1
              if check == 3:
                end_game = True 

              check = 0
              for _col, _row in zip(range(3), range(2, -1, -1)):
                if STATUS[matrix[_row][_col][1]] == current_turn:
                  check += 1
              if check == 3:
                end_game = True

  pygame.display.update()
  if end_game:
    print(f'{current_turn} 승리')
    pygame.time.delay(3000)
    run = False

pygame.quit()