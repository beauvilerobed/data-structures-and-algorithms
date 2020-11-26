# python3


# Hashing with chains


# Task. In this task your goal is to implement a hash table with
# lists chaining. You are already given the number of buckets 𝑚 and
# the hash function. It is a polynomial hash function

# h(𝑆) = (∑︁ 𝑆[𝑖]𝑥^𝑖 mod 𝑝) mod 𝑚, from 𝑖=0 to 𝑖=|S|-1

# where 𝑆[𝑖] is the ASCII code of the 𝑖-th symbol of 𝑆,
# 𝑝 = 1,000,000,007 and 𝑥 = 263. Your program should support
# the following kinds of queries:

# ∙ add string — insert string into the table. If there is already
# such string in the hash table, then just ignore the query.

# ∙ del string — remove string from the table. If there is no such
# string in the hash table, then just ignore the query.

# ∙ find string — output “yes" or “no" (without quotes) depending
# on whether the table contains string or not.

# ∙ check 𝑖 — output the content of the 𝑖-th list in the table.
# Use spaces to separate the elements of the list. If 𝑖-th list is
# empty, output a blank line.

# When inserting a new string into a hash chain, you must insert
# it in the beginning of the chain.

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(bucket_count)]
        self.responses = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        val = 'yes' if was_found else 'no'
        self.responses.append(val)

    def write_chain(self, chain):
        val = ' '.join(chain)
        self.responses.append(val)

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if query.ind not in range(self.bucket_count):
                return
            else:
                self.write_chain(self.elems[query.ind])
        else:
            chain = self.elems[self._hash_func(query.s)]

            if query.type == 'find':
                for val in chain:
                    if val == query.s:
                        self.write_search_result(True)
                        return
                self.write_search_result(False)
                return

            elif query.type == 'add':
                for val in chain:
                    if val == query.s:
                        return
                ind = self._hash_func(query.s)
                self.elems[ind].insert(0, query.s)
            else:
                for val in chain:
                    if val == query.s:
                        ind = self._hash_func(query.s)
                        self.elems[ind].remove(query.s)

    def process_queries(self):
        n = int(input())
        for _ in range(n):
            self.process_query(self.read_query())


def main():
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()


if __name__ == '__main__':
    main()
