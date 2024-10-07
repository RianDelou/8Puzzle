# node.py

class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def get_path(self):
        path = []
        current_node = self
        while current_node.parent is not None:
            path.append(current_node.move)
            current_node = current_node.parent
        path.reverse()
        return path
