import unittest
from lcs2 import lcs2
import random

def reference(seq1, seq2):
    count = 0
    index = 0
    
    for i in range(len(seq2)):
        for j in range(index, len(seq1)):
            if seq1[j] == seq2[i]:
                index = j + 1 
                count = count + 1
                break

    return count

class LCS2(unittest.TestCase):
    def test(self):
        for first_sequence, second_sequence, answer in (
            ((1, 2), (2, 1), 1),
            ((1, 2), (3, 4), 0),
            ([17] * 50, [17] * 25, 25),
            ([1] * 100, [1] * 100, 100),
            ((2, 7, 5), (2, 5), 2),
            ((7, ), (1, 2, 3, 4), 0),
            ((2, 7, 8, 3), (5, 2, 8, 7), 2),
            ((7, 2, 9, 3, 1, 5, 9, 4), (2, 8, 1, 3, 9, 7), 3)
        ):
            self.assertEqual(lcs2(first_sequence, second_sequence), answer)

    def test_stress(self):
        low = 0
        high = 10000
        columns = 50
        rows = 10000
        random_sequences = [random.choices(range(low, high), k=random.randrange(columns)) for _ in range(rows)]
        for i in range(0, rows, 2):
            first_sequence = random_sequences[i]
            second_sequence = random_sequences[i+1]
            self.assertEqual(lcs2(first_sequence, second_sequence), reference(first_sequence, second_sequence))


if __name__ == '__main__':
    unittest.main()