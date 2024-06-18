"""Project: Working with Sequences and Series
Start: June 18th 2024
Last touched: June 18th, 2024
Author: Madeleine L.
"""

import math

def recursive_sequence(n):
    if n < 1:
        return []
    # Initialize the sequence with the base cases for a_1 and a_2
    seq = [100, 21]

    for i in range(2, n):
        a_n = seq[i - 2]
        a_n1 = seq[i - 1]
        floor = math.floor((a_n + a_n1) / 2)
        ceiling = math.ceil(math.sqrt(a_n * a_n1))
        a_n2 = floor + ceiling
        seq.append(a_n2)
        print(f"n:{i+1} seq[{i+1}]: {seq[i]}\nfloor: {floor} ceiling: {ceiling}\n")
    return seq


sequence_calc = recursive_sequence(20)

print(f"First twenty terms: {sequence_calc}")

sum_of_terms = sum(sequence_calc)
print(f"Sum of first twenty terms: {sum_of_terms}")


