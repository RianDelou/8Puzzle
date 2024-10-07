# iterative_deepening_dfs.py

from node import Node

class IterativeDeepeningDFS:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def iterative_deepening_search(self, max_depth):
        for depth in range(max_depth + 1):
            result = self.depth_limited_search(Node(self.initial_state), depth)
            if result:
                return result.get_path()
        return None

    def depth_limited_search(self, node, limit):
        if node.state.is_goal_state(self.goal_state.board):
            return node
        elif node.depth >= limit:
            return None
        else:
            for new_state in node.state.generate_possible_moves():
                child_node = Node(new_state, parent=node, move=new_state.board, depth=node.depth + 1)
                result = self.depth_limited_search(child_node, limit)
                if result:
                    return result
        return None
