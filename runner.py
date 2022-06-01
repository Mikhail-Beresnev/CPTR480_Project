from numpy import void
from chess_ai import *
import chess
import chess.svg
import copy

# white = true
# black = false

white_pieces = ["P", "N", "B", "R", "Q", "K"]
black_pieces = ["p", "n", "b", "r", "q", "k"]

def main():
    board = chess.Board()
    user_color = user_chosen_color()
    ai_color = not user_color
    while True:
        print()
        print(board)
        user_move = user_chosen_move(board)
        board = result(board, user_move)
        check_terminal(board)

        ai_move = minimax(copy.deepcopy(board), 3)
        board = result(board, ai_move)
        check_terminal(board)
        print("Evaltion of position: " + str(utility(board)))

def check_terminal(board: chess.Board) -> void:
    if terminal(board):
            print(board)
            print("Winner: " + winner(board))
            quit()

def user_chosen_move(board: chess.Board) -> chess.Move:
    while True:
        move = input('Enter a move: ').strip()
        try:
            move = chess.Move.from_uci(move)
            if move in board.legal_moves:
                return move
            else:
                print("Please enter a valid move")
                print(board.legal_moves)
        except:
            print("ERROR: Please enter a valid move")

def user_chosen_color() -> chess.Color:
    while True:
        color = input('Choose color (White or Black): ').lower().strip()
        color = color.lower().strip() # lowercase and remove extra spaces
        if color == 'white':
            return chess.WHITE
        elif color == 'black':
            return chess.BLACK
        else:
            continue

def display_board(board: chess.Board) -> void:
    #calls the SVG render fuction, passes the above board and specifies the size in pixels. 
    boardsvg = chess.svg.board(board, size=350)

    #creates a file with proper permissions
    outputfile = open('board.svg', "w")
    outputfile.write(boardsvg)
    outputfile.close()

if __name__ == "__main__":
    main()