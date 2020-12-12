# python3

from collections import namedtuple, defaultdict

Clause = namedtuple('Clause', 'left right')


def read_file(file):
    with open(file) as f:
        lines = f.readlines()
        n = int(lines[0])
        clauses = []
        for line in lines[1:]:
            vals = list(map(int, line.split()))
            clause = Clause(vals[0], vals[1])
            clauses.append(clause)
        
        return clauses, n


def reduce_size(clauses):
    pos = {clause.left for clause in clauses if clause.left > 0} | \
          {clause.right for clause in clauses if clause.right > 0}
    neg = {-clause.left for clause in clauses if clause.left < 0} | \
          {-clause.right for clause in clauses if clause.right < 0}
    
    diff = pos.symmetric_difference(neg)
    
    while len(diff):
        i = 0
        while i < len(clauses):
            if abs(clauses[i].left) in diff or abs(clauses[i].right) in diff:
                clauses.pop(i)
            i += 1
        pos = {clause.left for clause in clauses if clause.left > 0} | \
              {clause.right for clause in clauses if clause.right > 0}
        neg = {-clause.left for clause in clauses if clause.left < 0} | \
              {-clause.right for clause in clauses if clause.right < 0}
        diff = pos.symmetric_difference(neg)
    return clauses
