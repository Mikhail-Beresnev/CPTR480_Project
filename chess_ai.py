import string
import chess
import copy

white_pieces = ["P", "N", "B", "R", "Q", "K"]
black_pieces = ["p", "n", "b", "r", "q", "k"]

piece_value = {
    "p": 1,
    "n": 3,
    "b": 3,
    "r": 5,
    "q": 9,
    "k": 1000
}

def winner(board: chess.Board) -> string:
    """
    Returns the winner of the game, if there is one.
    """
    if board.outcome().winner == chess.WHITE:
        return "White"
    elif board.outcome().winner == chess.WHITE:
        return "Black"
    else:
        return "Stalemate"


def player(board: chess.Board) -> chess.Color:
    """
    Returns player who has the current turn on a board
    """
    return board.turn

def actions(board: chess.Board) -> list:
    """
    Returns set of all possible actions available on the board
    """
    return board.legal_moves

def terminal(board: chess.Board) -> bool:
    """
    Returns True if game is over, False otherwise
    """
    if board.outcome() is not None:
        return True
    else:
        return False

def result(board: chess.Board, action: chess.Move) -> chess.Board:
    """
    Returns the board that results from making a move on the board
    """
    board.push(action)
    return board

def utility(board: chess.Board) -> int:
    """
    Returns a calculated value of all the pieces on the board
    """
    # terminal states
    if board.outcome() is not None:
        if board.outcome().result() == "1-0":
            # white wins
            return 100000
        elif board.outcome().result == "0-1":
            # black wins
            return -100000
        else:
            # stalemate
            return 0
    # count pieces
    white_value = 0
    black_value = 0
    for piece in board.fen():
        if piece == ' ':
            # stop counting once reaching end of board
            break
        if piece in white_pieces:
            # positive value if white piece
            white_value += piece_value.get(piece.lower())
        elif piece in black_pieces:
            # negative value if black piece
            black_value -= piece_value.get(piece.lower())
    return white_value + black_value

def minimax(board: chess.Board, max_depth: int) -> chess.Move:
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    aiSymbol = player(board)
    # set to opposite of desired goal so that it can achieve something
    if aiSymbol is chess.WHITE:
        best = float('-inf')
    elif aiSymbol is chess.BLACK:
        best = float('inf')
    else:
        raise Exception

    move = ()
    moveValue = 0
    alpha = float('-inf')
    beta = float('inf')

    for action in actions(board):
        if aiSymbol is chess.WHITE:
            # maximize the value
            moveValue = maxValue(result(copy.deepcopy(board),action), alpha, beta, 0, max_depth)
        elif aiSymbol is chess.BLACK:
            # minimuze the value
            moveValue = minValue(result(copy.deepcopy(board),action),alpha, beta, 0, max_depth)

        if aiSymbol is chess.WHITE and moveValue > best or aiSymbol is chess.BLACK and moveValue < best:
            del move
            move = action
            best = moveValue
    return move

def maxValue(board: chess.Board, alpha, beta, depth: int, max_depth: int):
    if terminal(board) or depth == max_depth:
        # num = utility(board)
        # if num != 0:
        #     print(board)
        #     print("evaluation: " + str(num))
        #     print('--------------------------')
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, minValue(result(copy.deepcopy(board), action), alpha, beta, depth+1, max_depth))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v

def minValue(board: chess.Board, alpha, beta, depth: int, max_depth: int):
    if terminal(board) or depth == max_depth:
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, maxValue(result(copy.deepcopy(board), action), alpha, beta, depth+1, max_depth))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v