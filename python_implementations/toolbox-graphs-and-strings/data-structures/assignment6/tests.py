import unittest
from unittest import mock
from hash_chains import Query, QueryProcessor
import hash_chains
import glob
import os
from io import StringIO

path = os.getcwd() + "/tests/*"
files = glob.glob(path)
files.sort()

solutions = list()
bucket_counts = list()

for name in files:
    with open(name, 'r') as f:
        if name[-2:] == ".a":
            lines = f.readlines()
            strings = list(map(lambda x: str(x)[:-1], lines))
            solutions = strings
        else:
            lines = f.read()
            bucket_counts = lines.split() 

## still needs work ##
# class TestQueryProcessor(unittest.TestCase):
#     @mock.patch('sys.stdout', new_callable=StringIO)
#     def main_op(self, tst_str, mock_stdout):
#         with mock.patch('builtins.input', side_effect=tst_str):
#             hash_chains.main()
        
#         return mock_stdout.getvalue()
    
#     def test(self):
#         for bucket_count, string in zip(bucket_counts, solutions):
#             print(self.main_op(bucket_count))


if __name__ == '__main__':
    unittest.main()