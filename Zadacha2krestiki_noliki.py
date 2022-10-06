# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1, 10))

def draw_board(board):
   for i in range(3):
      print( board[0+i*3], board[1+i*3], board[2+i*3])

def take_input(player_token):
   valid = False
   while not valid:
      answer = input("Where would you like to place " + player_token+"? ")
      try:
         answer = int(answer)
      except:
         print("Error. Try again. ")
         continue
      if answer >= 1 and answer <= 9:
         if(str(board[answer-1]) not in "XO"):
            board[answer-1] = player_token
            valid = True
         else:
            print("It's already busy. Try another one")
      else:
        print("Error. Enter numbers from 1 to 9.")

def check_win(board):
   winer = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in winer:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "won!")
              win = True
              break
        if counter == 9:
            print("Draw")
            break

main(board)
