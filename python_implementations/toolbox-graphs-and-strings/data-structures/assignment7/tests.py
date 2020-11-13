import unittest
from file_reader import generate_files, generate_test_case


files = generate_files()
trees, solutions = generate_test_case(files)


class TestQueryProcessor(unittest.TestCase):    
    def test_case(self):
        for tree, solution in zip(trees, solutions):
            actual = [
                " ".join(str(x) for x in tree.inOrder()),
                " ".join(str(x) for x in tree.preOrder()),
                " ".join(str(x) for x in tree.postOrder())
            ]
            self.assertEqual(actual, solution)


if __name__ == '__main__':
    unittest.main()