from itertools import permutations
import time


def find_combinations(s):
    combs = [''.join(p) for p in permutations(s)]
    return set(combs)

def save_combinations_to_file(input_string, filename="combinations.txt"):
    start_time = time.time()
    combinations = find_combinations(input_string)
    time_taken = time.time() - start_time
    with open(filename, "w") as f:
        f.write(f"--- Inputted: {input_string}, found all combinations in {time_taken:.4f} seconds ---\n")
        for comb in combinations:
            f.write(f"{comb}\n")
    print(f"Combinations saved to {filename}")

input_string = ""
save_combinations_to_file(input_string)