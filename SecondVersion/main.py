import time
from puzzle_state import PuzzleState
from iterative_deepening_direct_modification import IterativeDeepeningDFSDirectModification

def print_board(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else ' ' for num in row))

def main():
    # Lista de exemplos de estados iniciais e objetivos
    puzzles = [
        {
            "initial": [
                [1, 0, 3],
                [4, 2, 6],
                [7, 5, 8]
            ],
            "goal": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ]
        },
        {
            "initial": [
                [1, 2, 3],
                [4, 6, 0],
                [7, 5, 8]
            ],
            "goal": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ]
        },
        {
            "initial": [
                [1, 2, 3],
                [5, 0, 6],
                [4, 7, 8]
            ],
            "goal": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ]
        },
        {
            "initial": [
                [4, 1, 3],
                [7, 2, 5],
                [0, 8, 6]
            ],
            "goal": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ]
        }
    ]

    for index, puzzle in enumerate(puzzles):
        initial_board = puzzle["initial"]
        goal_board = puzzle["goal"]

        print(f"\nResolving Puzzle {index + 1}")
        print("Estado inicial:")
        print_board(initial_board)
        print("\nEstado objetivo:")
        print_board(goal_board)

        initial_state = PuzzleState(initial_board)
        goal_state = PuzzleState(goal_board)

        search = IterativeDeepeningDFSDirectModification(initial_state, goal_state)

        start_time = time.time()
        solution_path = search.iterative_deepening_search(max_depth=20)
        end_time = time.time()
        execution_time = end_time - start_time

        if solution_path:
            print("\nSolução encontrada! Caminho:")
            for move in solution_path:
                print_board(move)
                print()  
            print(f"Tempo de execução para o Puzzle {index + 1}: {execution_time:.4f} segundos")
        else:
            print("Solução não encontrada dentro da profundidade máxima.")
            print(f"Tempo de execução para o Puzzle {index + 1}: {execution_time:.4f} segundos")

if __name__ == "__main__":
    main()
