# puzzle_state.py

import copy

class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.empty_pos = self.find_empty()

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:  # 0 representa o espaço vazio
                    return (i, j)

    def is_goal_state(self, goal_board):
        return self.board == goal_board

    def generate_possible_moves(self):
        moves = []
        i, j = self.empty_pos
        possible_positions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for new_i, new_j in possible_positions:
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                new_board = copy.deepcopy(self.board)
                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                moves.append(PuzzleState(new_board))

        return moves
