import unittest
from primitive_calculator import compute_operations

def reference(n):
	result = [0, [0, [1]]]
	
	for k in range(2, n + 1):
		values = result[k - 1]
		if k % 2 == 0:
			if result[k // 2][0] < values[0]:
				values = result[k // 2]
		
		if k % 3 == 0:
			if result[k // 3][0] < values[0]:
				values = result[k // 3]

		next_value = values[0] + 1
		next_array = values[1] + [k]				
		result.append([next_value, next_array])

    
	return result[-1][1]

class PrimitiveCalculator(unittest.TestCase):
    def test(self):
        for n, answer in ((2, 1), (3, 1), (5, 3), (10, 3)):
            sequence = reference(n)
            self.assertEqual(answer, len(sequence) - 1)
            self.assertEqual(sequence[0], 1)
            self.assertEqual(sequence[-1], n)
            for i in range(len(sequence) - 1):
                if sequence[i + 1] != sequence[i] + 1 and sequence[i + 1] != 2 * sequence[i]:
                    self.assertEqual(sequence[i + 1], 3 * sequence[i])


if __name__ == '__main__':
    unittest.main()