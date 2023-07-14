#Set up variables and imports
import random
import os
board = [['1','2','3','4','5','6'],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ']]

game_running = True

#Randomly chooses who goes first
player = random.choice(['Red','Blue'])

#Print board function
def print_board():
  for horizontal_line in board:
    print(horizontal_line)


#Update player function
def update_player(player):
  if player == 'Red':
    player = 'Blue'
  elif player == 'Blue':
    player = 'Red'
  return player
    
#Update board function - prompts for input from player, finds lowest open spot in selected column
def update_board():
  global player
  col = input(f'\n{player} player, which column (1, 2, 3, 4, 5, 6) do you want to drop your token into?')
  column = int(col) - 1
  for row in reversed(board):
    if row[column] == ' ':
      row[column] = player[0]
      break
  
#Checking for horizontal wins
def check_horizontal(player):
  letter = player[0]
  global game_running
  for row in board:
    count = 0
    for space in row:
      if space == letter:
        count += 1
        if count >= 4:
          game_running = False
          break
      else:
        count = 0

#Checking for vertical wins
def check_vertical(player):
  letter = player[0]
  global game_running
  for column in range(0,6):
    count = 0
    for row in board:
      if row[column] == letter:
        count += 1
        if count >= 4:
          game_running = False
          break
      else:
        count = 0

#checking for diagonal wins, with diagonals going to the right
def check_diagonal_right(player):
  letter = player[0]
  global game_running
  for row in range(4,8):
    for col in range (0,3):
      if board[row][col] == letter:
        if board[row-1][col+1] == letter:
          if board[row-2][col+2] == letter:
            if board[row-3][col+3] == letter:
              game_running = False
              break

#Checking for diagonal wins with diagonals going to the left
def check_diagonal_left(player):
  letter = player[0]
  global game_running
  for row in range(4,8):
    for col in range (3,6):
      if board[row][col] == letter:
        if board[row-1][col-1] == letter:
          if board[row-2][col-2] == letter:
            if board[row-3][col-3] == letter:
              game_running = False
              break


#Game loop
while game_running:
  print_board()
  update_board()
  check_horizontal(player)
  check_vertical(player)
  check_diagonal_right(player)
  check_diagonal_left(player)
  player = update_player(player)
  os.system('clear')

#Prints out the winner
player = update_player(player)
print(f'{player} wins')