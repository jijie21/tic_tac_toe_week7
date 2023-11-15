from logic import check_winner, get_empty_board, print_board, get_player_input, switch_player
import logging
# add the log file record the games 
logging.basicConfig(
    filename='log/msg.log',
    level=logging.INFO
)
         

if __name__ == '__main__': #program excute directly
    current_player = "X"
    board = get_empty_board()
    winner = None 
    
    while winner is None: 
        print_board(board)
        try:
           row, col = get_player_input(current_player)
        
        except ValueError:
            print("Invaild, try again")
            continue
        except IndexError:
            print("Invaild, try again")
            continue

        print(row)
        print(col)

        board[row][col] = current_player
        winner = check_winner(board)
        current_player = switch_player(current_player)
print_board(board)
print(f"winner is {winner}")
logging.info(f'Player {current_player} made a move')