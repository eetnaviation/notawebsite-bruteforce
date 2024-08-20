import itertools
import time

# Load the list of common words from a file
with open('../words.txt', 'r') as file:
    words = file.read().splitlines()

# Generate all combinations of two words
start_time = time.time()

# Using itertools.product to create combinations on the CPU
combinations = itertools.product(words, repeat=2)

# Combine the tuples into strings (word1 + word2)
combined_words = [word1 + word2 for word1, word2 in combinations]

# Save the combined words to a file
output_filename = 'combined_words.txt'
with open(output_filename, 'w') as file:
    for word in combined_words:
        file.write(f"{word}\n")

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Combined words saved to {output_filename}")
