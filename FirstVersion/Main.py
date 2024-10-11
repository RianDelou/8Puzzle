from puzzle_state import PuzzleState
from iterative_deepening_DFS import IterativeDeepeningDFS
import time

def count_inversions(board):


    flat_list = [num for row in board for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                inversions += 1
    return inversions

def is_solvable(board):
    inversions = count_inversions(board)
    return inversions % 2 == 0

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

    for index, puzzle in enumerate(puzzles, start=1):
        initial_board = puzzle["initial"]
        goal_board = puzzle["goal"]

        print(f"\nPuzzle {index}:")
        print("Estado inicial:")
        print_board(initial_board)
        print("\nEstado objetivo:")
        print_board(goal_board)

        try:
            inversions = count_inversions(initial_board)
            if not is_solvable(initial_board):
                raise ValueError(f"O puzzle não é resolvível com esse estado inicial. Número de inversões ímpar: {inversions}")
            
            print("\nO puzzle é resolvível!")

           
            initial_state = PuzzleState(initial_board)
            goal_state = PuzzleState(goal_board)

            search = IterativeDeepeningDFS(initial_state, goal_state)

            start_time = time.time()
            solution_path = search.iterative_deepening_search(max_depth=20)
            end_time = time.time()
            execution_time = end_time - start_time

            if solution_path:
                print("\nSolução encontrada! Caminho:")
                for move in solution_path:
                    print_board(move)
                    print()  
                print(f"Tempo de execução: {execution_time:.4f} segundos")
            else:
                print("Solução não encontrada dentro da profundidade máxima.")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
