# python3


def is_true(clauses, i, bools):
    left = clauses[i].left
    right = clauses[i].right
    x1 = not bools[-left] if left < 0 else bools[left]
    x2 = not bools[-right] if right < 0 else bools[right]

    return x1 or x2
