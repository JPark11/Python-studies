from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

intro = """
In this game, you will attempt to sink my battleship hidden among the ocean that conveniently looks like a board made of letter Os.

Guess the location of the hidden ship by entering the row and column number.
Choose numbers between 1 and 5!

You have 10 guesses in total.
"""
print("="*80)
print("\nWelcome to Battleship!\n")
print_board(board)
print(intro)
print("="*80)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#print(ship_row)
#print(ship_col)

for turn in range(10):
  print("\nTurn", turn + 1, "\n")
  print_board(board)
  print(" ")

  try:
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Column: ")) - 1
  except:
    print("\nCHOOSE NUMBERS BETWEEN 1 AND 5")
    continue
  
  print(" ")

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if turn == 9:
      print("="*80)
      print("\nGame Over X_X")
      print("The ship was hidden at row %d, column %d.\n" % (ship_row+1, ship_col+1)) 
      board[ship_row][ship_col] = "S"
      print_board(board)

#mode: random/pvp, difficulty setting: easy, medium, hard / board size
    
