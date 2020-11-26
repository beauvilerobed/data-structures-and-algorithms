import unittest
from hash_chains import Query, QueryProcessor
from file_reader import generate_files, generate_test_case


files = generate_files()
info, solution = generate_test_case(files)


class TestQueryProcessor(unittest.TestCase):
    def test_case(self):
        bucket_count = info[0]
        proc = QueryProcessor(bucket_count)
        for query in info[1:]:
            proc.process_query(query)
        self.assertEqual(proc.responses, solution)


if __name__ == '__main__':
    unittest.main()
