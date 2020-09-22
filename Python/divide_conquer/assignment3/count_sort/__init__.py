global global_count
global_count = 0

def count_sort(input_array, choose_pivot):
  partition_around_array(input_array, 0, len(input_array) - 1, choose_pivot)
  global global_count
  count = global_count
  global_count = 0
  return count 

def partition_around_array(input_array, left, right, choose_pivot):
  global global_count
  global_count += max(right - left, 0)
  if right - left < 1:
    return 
  
  pivot_index = select_first(left, right)
  if choose_pivot == 'right':
    pivot_index = select_last(left, right)
  elif choose_pivot == 'middle':
    pivot_index = select_middle(input_array, left, right)

  input_array[left], input_array[pivot_index] = input_array[pivot_index], input_array[left]

  i = left + 1
  for j in range(left + 1, right + 1):
    if input_array[j] < input_array[left]:
      input_array[i], input_array[j] = input_array[j], input_array[i]
      i += 1

  input_array[left], input_array[i-1] = input_array[i-1], input_array[left]

  if i != left + 1:
    partition_around_array(input_array, left, i-2, choose_pivot)
  partition_around_array(input_array, i, right, choose_pivot)

def select_first(left, right):
  return left
 
def select_last(left, right):
  return right

def select_middle(input_array, left, right):
  middle = left + ((right - left) // 2)
  median = median_value([input_array[left], input_array[right], input_array[middle]])
  middle_index = input_array.index(median)
  return middle_index

def median_value(input_array):
  if len(input_array) == 0:
    return 0

  input_array.sort()  
  middle_index = len(input_array) // 2
  if len(input_array) % 2:
    return input_array[middle_index]
  return (input_array[middle_index - 1] + input_array[middle_index]) / 2
  