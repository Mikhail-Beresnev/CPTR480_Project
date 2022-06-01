from chess_ai import *
import unittest

class Test(unittest.TestCase):
    def test_winner(self):
        winning_board = chess.Board('R6k/1R6/8/8/8/8/8/7K b - - 0 1')
        self.assertEqual(winner(winning_board), "White")
    
    def test_player(self):
        position = chess.Board()
        self.assertEqual(player(position), chess.WHITE)
    
    def test_actions(self):
        position = chess.Board('7k/R7/1R6/8/8/8/8/7K b - - 0 1')
        test_move = ""
        for move in actions(position):
            test_move = move
        self.assertEqual(test_move, chess.Move.from_uci("h8g8"))

    def test_terminal(self):
        terminal_board = chess.Board('R6k/1R6/8/8/8/8/8/7K b - - 0 1')
        self.assertEqual(terminal(terminal_board), True)
    
    def test_result(self):
        board = chess.Board()
        end_board = chess.Board('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        self.assertEqual(result(board, chess.Move.from_uci("e2e4")), end_board)

    def test_utility(self):
        board = chess.Board('7k/8/8/8/8/8/8/1Q5K b - - 0 1')
        self.assertEqual(utility(board), 9)


if __name__ == "__main__":
    unittest.main()