# tic-tac-toe


## Python을 이용한 Tic Tac Toe 만들기
### pygame
 
### 상수정의
```python
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WINDOW_SIZE = 550
RECT_SIZE = 150
CIRCLE_SIZE = 50
BLANK_SIZE = 25
LINE_SIZE = 3
STATUS = ['O', 'X', None]
TURNS = ['O', 'X']
```
### 정사각형 칸 만들기
```python
matrix = [[[pygame.draw.rect(window, WHITE, (BLANK_SIZE * (col + 1) + RECT_SIZE * col, BLANK_SIZE * (row + 1) + RECT_SIZE * row, RECT_SIZE, RECT_SIZE)), -1] for col in  range(3)] for row in range(3)]
```
### O의 순서인지 X의순서인지 구분
```python
run = True
end_game = False
true_value = 0
current_turn = TURNS[true_value%2]
```
### 어느칸을 클릭한지 파악하고 O/X를 그리고 승리 조건을 판단
```python
if event.type == pygame.MOUSEBUTTONUP:
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
```
### 가로확인
```python
              for _row in range(3):
                check = 0
                for _col in range(3):
                  if STATUS[matrix[_row][_col][1]] == current_turn:
                    check += 1
                if check == 3:
                  end_game = True
```
### 세로확인
```python
              for _col in range(3):
                check = 0
                for _row in range(3):
                  if STATUS[matrix[_row][_col][1]] == current_turn:
                    check += 1
                if check == 3:
                  end_game = True
                  
```
### 우대각확인
```python
              check = 0 
              for _col, _row in zip(range(3), range(3)):
                if STATUS[matrix[_row][_col][1]] == current_turn:
                  check += 1
              if check == 3:
                end_game = True 
```
### 좌대각확인
```python
              check = 0
              for _col, _row in zip(range(3), range(2, -1, -1)):
                if STATUS[matrix[_row][_col][1]] == current_turn:
                  check += 1
              if check == 3:
                end_game = True
```
### 현재 상태 업데이트 및 게임이 끝나면 반복문과 pygame 종료
```python
  pygame.display.update()
  if end_game:
    print(f'{current_turn} 승리')
    pygame.time.delay(3000)
    run = False
```
