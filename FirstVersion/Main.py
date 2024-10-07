# main.py

from puzzle_state import PuzzleState
from iterative_deepening_DFS import IterativeDeepeningDFS

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

def main():
    # Definindo o estado inicial do tabuleiro (8-puzzle)
    initial_board = [
        [1, 2, 3],
        [4, 0, 6],  # 0 representa o espaço vazio
        [7, 5, 8]
    ]

    goal_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    try:
        inversions = count_inversions(initial_board)
        if not is_solvable(initial_board):
            raise ValueError(f"O puzzle não é resolvível com esse estado inicial. Número de inversões ímpar: {inversions}")
        
        print("O puzzle é resolvível. Iniciando a busca...")

        # Criando o estado inicial e objetivo
        initial_state = PuzzleState(initial_board)
        goal_state = PuzzleState(goal_board)

        # Criando a busca com Iterative Deepening Depth-First Search
        search = IterativeDeepeningDFS(initial_state, goal_state)

        # Executando a busca iterativa em profundidade
        solution_path = search.iterative_deepening_search(max_depth=20)

        if solution_path:
            print("Solução encontrada! Caminho:")
            for move in solution_path:
                print(move)
        else:
            print("Solução não encontrada dentro da profundidade máxima.")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
