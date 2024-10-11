class IterativeDeepeningDFSDirectModification:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def depth_limited_search(self, state, depth):
        if state.is_goal(self.goal_state):
            return [state.get_board()]

        if depth == 0:
            return None

        for move in state.get_possible_moves():
            state.move_blank(move)
            path = self.depth_limited_search(state, depth - 1)
            if path:
                return [state.get_board()] + path
            state.undo_move(move)

        return None

    def iterative_deepening_search(self, max_depth):
        for depth in range(max_depth + 1):
            result = self.depth_limited_search(self.initial_state, depth)
            if result:
                return result
        return None
