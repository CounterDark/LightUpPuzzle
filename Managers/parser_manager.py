import argparse

def init_parser():
    parser = argparse.ArgumentParser(description="Program rozwiązujący zagadkę LightUp przy użyciu różnych algorytmów")

    parser.add_argument("algorithm", type=str, choices=["hill_climb", "tabu", "hill_climb_stochastic", "brute_force"],
                        help="Nazwa algorytmu do użycia (np. brute_force, hill_climb, tabu)")

    parser.add_argument("-i", "--input_file", type=str,
                        help="(Opcjonalny) Ścieżka do pliku wejściowego z zagadką")

    parser.add_argument("-o", "--output_file", type=str,
                        help="(Opcjonalny) Ścieżka do pliku wyjściowego")

    parser.add_argument("-v", "--verbose", action="store_true",)

    parser.add_argument("-k" , type=int, help="Ilość iteracji algorytmu. Domyślnie: 4000")

    return parser