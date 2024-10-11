class IterativeDeepeningDFSDirectModification:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def depth_limited_search(self, state, depth, path):
        if state.is_goal(self.goal_state):
            return path + [state.get_board()]

        if depth == 0:
            return None

        for move in state.get_possible_moves():
            state.move_blank(move)
            new_path = path + [state.get_board()]
            result = self.depth_limited_search(state, depth - 1, new_path)
            if result:
                return result
            state.undo_move(move)

        return None

    def iterative_deepening_search(self, max_depth):
        for depth in range(max_depth + 1):
            result = self.depth_limited_search(self.initial_state, depth, [])
            if result:
                return result
        return None
