class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.size = len(board)

    def find_blank_space(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j
        return None

    def get_possible_moves(self):
        row, col = self.find_blank_space()
        moves = []
        if row > 0:
            moves.append((-1, 0))  
        if row < self.size - 1:
            moves.append((1, 0))   
        if col > 0:
            moves.append((0, -1))  
        if col < self.size - 1:
            moves.append((0, 1))   
        return moves

    def move_blank(self, move):
        row, col = self.find_blank_space()
        new_row, new_col = row + move[0], col + move[1]
        self.board[row][col], self.board[new_row][new_col] = self.board[new_row][new_col], self.board[row][col]

    def undo_move(self, move):
        self.move_blank((-move[0], -move[1]))

    def is_goal(self, goal_state):
        return self.board == goal_state.board

    def get_board(self):
        return [row[:] for row in self.board]
