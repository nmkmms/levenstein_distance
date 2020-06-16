"""Find all words from file which has no more then given Levenstein distance to given word."""
import os
# ==================================================
# USER INPUT:

# File with words
FILENAME = 'enwiki-small-cen.txt'

# Word to search
CODE_WORD = 'Algebra'

# Maximum Leventstein distance
MAX_DISTANCE = 1

# END OF USER INPUT
# ==================================================


def main():
    """Call functions, struct code."""
    words = load_dictionary(FILENAME)

    # List, which contains 2 empty lists to contain results
    found = [[] for _ in range(MAX_DISTANCE)]

    # Filling lists 
    # Add word to first list, if L distance is 1
    # Add word to second list, if L distance is 2
    for word in words:
        if abs(len(CODE_WORD) - len(word)) > MAX_DISTANCE:
            continue
        distance = levenshtein(CODE_WORD, word)
        if distance in range(1, MAX_DISTANCE + 1):
            found[distance - 1].append(word)

    for i in range(MAX_DISTANCE):
        print(f"Words with Levenshtein distance {i + 1} to word {CODE_WORD}:")
        for word in found[i]:
            print(f"\t{word}")




def load_dictionary(filename: str) -> list:
    """Load file & return list."""
    # Add absolute path to file
    filepath = f"{os.getcwd()}/{filename}"
    with open(filepath) as in_file:
        words = (in_file.read()).split('\n')
        return words


def levenshtein(word1: str, word2: str, print_matrix=False) -> int:
    """Return Levenshtein distance between 2 words."""
    size_x = len(word1) + 1
    size_y = len(word2) + 1

    # Generate matrix with zeros and starting numbers
    matrix = [[0 for _ in range(size_x)] for _ in range(size_y)]
    for x in range(1, size_x):
        matrix [0][x] = x
    for y in range(1, size_y):
        matrix [y][0] = y

    # Filling matrix
    for x in range(1, size_x):
        for y in range(1, size_y):
            if word1[x - 1] == word2[y - 1]:
                matrix [y][x] = min(
                    matrix[y][x - 1] + 1,
                    matrix[y - 1][x - 1],
                    matrix[y - 1][x] + 1
                )
            else:
                matrix [y][x] = min(
                    matrix[y][x - 1] + 1,
                    matrix[y - 1][x - 1] + 1,
                    matrix[y - 1][x] + 1
                )

    # Output matrix (for test)
    if print_matrix:
        for line in matrix:
            print(line)

    return matrix[size_y - 1][size_x - 1]


if __name__ == '__main__':
    main()