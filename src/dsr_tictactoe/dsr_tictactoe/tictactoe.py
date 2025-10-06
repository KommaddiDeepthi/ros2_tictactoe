#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class TicTacToe(Node):
    def __init__(self):
        super().__init__('tictactoe_node')
        self.board = [" " for _ in range(9)]
        self.current_player = "X"  # User is X, Doosan is O
        self.play_game()

    def print_board(self):
        b = self.board
        print("\n")
        print(f"{b[0]} | {b[1]} | {b[2]}")
        print("--+---+--")
        print(f"{b[3]} | {b[4]} | {b[5]}")
        print("--+---+--")
        print(f"{b[6]} | {b[7]} | {b[8]}")
        print("\n")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def winner(self, board, player):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combos:
            if all(board[i] == player for i in combo):
                return True
        return False

    def minimax(self, board, depth, is_maximizing):
        if self.winner(board, "O"):
            return 1
        elif self.winner(board, "X"):
            return -1
        elif " " not in board:
            return 0

        if is_maximizing:
            best_score = -999
            for move in self.available_moves():
                board[move] = "O"
                score = self.minimax(board, depth + 1, False)
                board[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = 999
            for move in self.available_moves():
                board[move] = "X"
                score = self.minimax(board, depth + 1, True)
                board[move] = " "
                best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -999
        move = None
        for i in self.available_moves():
            self.board[i] = "O"
            score = self.minimax(self.board, 0, False)
            self.board[i] = " "
            if score > best_score:
                best_score = score
                move = i
        return move

    def play_game(self):
        print("Welcome to TicTacToe! You are X. Doosan is O.")
        self.print_board()

        while True:
            if self.current_player == "X":
                try:
                    move = int(input("Enter your move (0-8): "))
                except ValueError:
                    print("Invalid input. Enter a number 0-8.")
                    continue
                if move not in self.available_moves():
                    print("Invalid move. Try again.")
                    continue
                self.board[move] = "X"
                self.current_player = "O"
            else:
                move = self.best_move()
                self.board[move] = "O"
                print(f"🤖 Doosan chooses position {move}")
                self.current_player = "X"

            self.print_board()

            if self.winner(self.board, "X"):
                print("🎉 You win! (That should be impossible 😅)")
                break
            elif self.winner(self.board, "O"):
                print("🤖 Doosan wins! Better luck next time.")
                break
            elif " " not in self.board:
                print("It's a draw!")
                break


def main(args=None):
    rclpy.init(args=args)
    node = TicTacToe()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
