import unittest
from build_heap import build_heap
from file_reader import generate_files, generate_test_case


files = generate_files()
solution, test_case = generate_test_case(files)


class MakeHeap(unittest.TestCase):
    def test(self):
        self.assertEqual(solution[1:], build_heap(test_case))

if __name__ == '__main__':
    unittest.main()
