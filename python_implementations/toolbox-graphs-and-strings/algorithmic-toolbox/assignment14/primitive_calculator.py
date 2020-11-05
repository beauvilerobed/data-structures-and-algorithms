

def compute_operations(n):
	result = [0, [0, [1]]]
	
	for k in range(2, n + 1):
        # find the min previously compute operation value
        # of k/2 k/3 (if they exist) and k - 1 dynamically
		values = result[k - 1]
		if k % 2 == 0:
			if result[k // 2][0] < values[0]:
				values = result[k // 2]
		
		if k % 3 == 0:
			if result[k // 3][0] < values[0]:
				values = result[k // 3]

        # then add to result of appropriate value
		next_value = values[0] + 1
		next_array = values[1].append(k)				
		result.append([next_value, next_array])

    
	return result[-1][1]


def main():
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)


if __name__ == '__main__':
    main()