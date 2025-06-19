import argparse

def init_parser():
    parser = argparse.ArgumentParser(description="Program rozwiązujący zagadkę LightUp przy użyciu różnych algorytmów")

    parser.add_argument("algorithm", type=str, choices=["hill_climb", "tabu", "hill_climb_stochastic", "brute_force", "annealing"],
                        help="Nazwa algorytmu do użycia (np. brute_force, hill_climb, tabu)")

    parser.add_argument("-i", "--input_file", type=str,
                        help="(Opcjonalny) Ścieżka do pliku wejściowego z zagadką")

    parser.add_argument("-o", "--output_file", type=str,
                        help="(Opcjonalny) Ścieżka do pliku wyjściowego")

    parser.add_argument("-v", "--verbose", action="store_true",)

    parser.add_argument("-k" , type=int, help="Ilość iteracji algorytmu. Domyślnie: 4000")

    parser.add_argument("--tabu_size", type=int, help="Rozmiar listy tabu (tylko dla tabu)")

    parser.add_argument("--start_temp", type=float, help="Początkowa temperatura wyżarzania")

    parser.add_argument("--alpha", type=float, help="Alpha do algorytmów")

    parser.add_argument("--temp_function", type=str, choices=['linear', 'exponential', 'log'], help="Rodzaj funkcji temperatury (tylko dla wyżarzania)")
    return parser