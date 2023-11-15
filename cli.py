from logic import check_winner, get_empty_board, print_board, get_player_input, switch_player
from bot import Bot
import logging

# dependency injection implementation
class TicTacToeGame:
    def __init__(self, mode):
        self.current_player = "X"
        self.board = get_empty_board()
        self.winner = None
        self.mode = mode
        self.bot = Bot()

    def play_game(self):
        while self.winner is None:
            print_board(self.board)
            
            if self.mode == "single" and self.current_player == "O":
                row, col = self.bot.get_bot_move(self.board)
            else:
                try:
                    row, col = get_player_input(self.current_player)
                except ValueError:
                    print("Invalid input, try again")
                    continue
                except IndexError:
                    print("Invalid input, try again")
                    continue

            self.board[row][col] = self.current_player
            self.winner = check_winner(self.board)
            self.current_player = switch_player(self.current_player)

        print_board(self.board)
        print(f"Winner is {self.winner}")
        logging.info(f'Player {self.current_player} made a move')


if __name__ == '__main__':
    logging.basicConfig(
        filename='log/msg.log',
        level=logging.INFO
    )

    game_mode = input("Enter game mode (single or two): ").lower()

    if game_mode not in ["single", "two"]:
        print("Invalid game mode. Exiting.")
        exit()

    game = TicTacToeGame(game_mode)
    game.play_game()
