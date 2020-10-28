import sys

def max_weight_IS(weights, length):
    possible_vertices = {0: 0, 1: 1, 2: 2, 3: 3, 16: 4, 116: 5, 516: 6, 996: 7}
    result = ['0' for _ in range(8)]

    max_weights = [0, weights[0]]

    for i in range(2, length):
        choice = int()
        if max_weights[i-1] > max_weights[i-2] + weights[i-1]:
            choice = max_weights[i-1]
            print(i)
        else:
            choice = max_weights[i-2] + weights[i-1]
        max_weights.append(choice)
    
    reconstructed_weights = []
    print(max_weights)
    i = len(max_weights)
    
    while i >= 0:
        if max_weights[i-1] >= max_weights[i-2] + weights[i - 1]:
            i = i - 1
        else:
            reconstructed_weights.append(i - 1)
            i = i - 2

    print(reconstructed_weights)
    for val in reconstructed_weights:
        if val in possible_vertices:
            result[possible_vertices[val]] = '1'
            
    return "".join(result)


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    length = data_set[0]
    print(max_weight_IS(data_set[1:], length))


if __name__ == '__main__':
    main()
    
