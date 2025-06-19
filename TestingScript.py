import subprocess
import time
import json
import matplotlib.pyplot as plt
import pandas as pd
import csv
import sys
from itertools import product

ALGORITHMS = ["hill_climb", "hill_climb_stochastic", "tabu", "brute_force"]
INPUT_FILE = "Resources/Boards/board1"
ITERATIONS = [100, 150, 500]
REPEATS = 2

PARAMETERS = {
    "tabu": {
        "tabu_size": [10, 50, 100]
    },
}

CSV_OUTPUT = "results.csv"

def run_algorithm(algo, k, input_file, extra_args=[]):
    cmd = [sys.executable, "main.py", algo, "-k", str(k), "-i", input_file, "-v"] + extra_args
    start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True)
    end_time = time.time()
    return result.stdout, end_time - start_time

def parse_completeness(output):
    for line in list(reversed(output.splitlines())):
        if "Completeness" in line:
            return float(line.strip().split()[-1])
    return 0.0

def parse_convergence(output):
    convergence = []
    for line in output.splitlines():
        if "Completeness" in line:
            try:
                val = float(line.strip().split()[-1])
                convergence.append(val)
            except:
                continue
    return convergence

def analyze_efficiency(results, target_precision=1):
    grouped = {}
    for row in results:
        rounded = round(row["completeness"], target_precision)
        key = f"{rounded:.{target_precision}f}"
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(row)

    for group in sorted(grouped.keys(), reverse=True):
        algorithms = grouped[group]
        # if len(algorithms) < 2:
        #     continue

        print(f"\nGroup  {group}:")
        best = min(algorithms, key=lambda r: r["duration"])
        print(f"Fastest: {best['algorithm']} {best['params']}")
        print(f"Duration: {best['duration']:.4f} s, Completeness: {best['completeness']:.{target_precision+3}f}")

def merge_with_variations(new_parameters, parameters_set):
    new_set = []
    for param_dict in parameters_set:
        keys = list(new_parameters.keys())
        for key in keys:
            values = new_parameters[key]
            new_set.extend({**{key: v}, **param_dict} for v in values)
    return new_set

def compare():
    results = {}

    for algo in ALGORITHMS:
        param_set = [{"iterations": it} for it in ITERATIONS]
        if algo in PARAMETERS:
            param_set = merge_with_variations(PARAMETERS[algo], param_set)

        for params in param_set:
            for r in range(REPEATS):
                extra_args = []
                if algo == "tabu" and "tabu_size" in params:
                    extra_args += ["--tabu_size", str(params["tabu_size"])]

                print(f"Running {algo}, params={params}, repeat={r+1}")
                output, duration = run_algorithm(algo, params["iterations"], INPUT_FILE, extra_args)
                print("Output: ", output)
                completeness = parse_completeness(output)
                convergence = parse_convergence(output)

                if algo not in results or results.get(algo, {}).get("completeness", 0.0) < completeness:
                    results[algo] = ({
                        "algorithm": algo,
                        "params": json.dumps(params),
                        "duration": duration,
                        "completeness": completeness,
                        "convergence": convergence
                    })
    return results

def save_to_csv(results, filename):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "params", "duration", "completeness", "convergence"])
        for row in results:
            writer.writerow([
                row["algorithm"],
                row["params"],
                f"{row['duration']:.4f}",
                f"{row['completeness']:.4f}",
                ";".join(f"{x:.4f}" for x in row["convergence"])
            ])

def plot_results(results):
    df = pd.DataFrame(results)

    # Duration
    plt.figure(figsize=(10, 5))
    grouped = df.groupby(["algorithm", "params"]).mean(numeric_only=True).reset_index()
    for i, row in grouped.iterrows():
        plt.bar(f"{row.algorithm}\n{row.params}", row.duration)
    plt.title("Duration")
    plt.ylabel("Time [s]")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # Completeness
    plt.figure(figsize=(10, 5))
    for i, row in grouped.iterrows():
        plt.bar(f"{row.algorithm}\n{row.params}", row.completeness)
    plt.title("Completeness")
    plt.ylabel("Completeness [0-1]")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # Best slope
    plt.figure(figsize=(10, 5))
    for row in results:
        if len(row["convergence"]) > 1:
            plt.plot(row["convergence"], label=f'{row["algorithm"]} ({row["params"]})')
    plt.title("Best slope")
    plt.xlabel("Iterations")
    plt.ylabel("Completeness")
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    results = compare()
    results_values = results.values()
    save_to_csv(results_values, CSV_OUTPUT)
    print(f"\nResults saved to: {CSV_OUTPUT}")
    plot_results(results_values)
    analyze_efficiency(results_values)
