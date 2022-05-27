import chess
import math

white = "white"
black = "black"

def main():
    board = chess.Board()
    print(board.outcome())

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return board.outcome()


def player(board):
    """
    Returns player who has the next turn on a board
    """
    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions available on the board
    """
    raise board.legal_moves

def terminal(board):
    """
    Returns True if game is over, False otherwise
    """
    if board.outcome() is not None:
        return True
    else:
        return False

def result(board, action):
    """
    Returns the board that results from making a move on the board
    """
    raise NotImplementedError

def utility(board):
    """
    Returns a calculated value of all the pieces on the board
    """
    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    move = ()
    aiSymbol = player(board)
    if aiSymbol is white:
        best = float('inf')
    elif aiSymbol is black:
        best = float('-inf')
    else:
        raise Exception
    
    moveValue = 0
    alpha = float('-inf')
    beta = float('inf')

    for action in actions(board):
        if aiSymbol is white:
            # maximize the value
            moveValue = maxValue(result(board,action), alpha, beta)
        elif aiSymbol is black:
            # minimuze the value
            moveValue = minValue(result(board,action),alpha, beta)

        if aiSymbol is white and moveValue < best or aiSymbol is black and moveValue > best:
            del move
            move = action
            best = moveValue
    return move

def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, minValue(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v

def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, maxValue(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v

if __name__ == "__main__":
    main()