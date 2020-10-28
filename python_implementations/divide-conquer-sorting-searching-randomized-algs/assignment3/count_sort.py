import sys
import statistics 
import copy


global global_count
global_count = 0

def count_sort(input_array, choose_pivot):

  def partition_around_array(input_array, left, right):
    global global_count
    global_count += max(right - left, 0)
    if right - left < 1:
      return 

    pivot_index = int()
    if choose_pivot == 'right':
      pivot_index = select_last(left, right)
    elif choose_pivot == 'middle':
      pivot_index = select_middle(input_array, left, right)
    elif choose_pivot == 'left':
      pivot_index = select_first(left, right)

    input_array[left], input_array[pivot_index] = input_array[pivot_index], input_array[left]

    i = left + 1
    for j in range(left + 1, right + 1):
      if input_array[j] < input_array[left]:
        input_array[i], input_array[j] = input_array[j], input_array[i]
        i += 1

    input_array[left], input_array[i-1] = input_array[i-1], input_array[left]

    if i != left + 1:
      partition_around_array(input_array, left, i-2)
    partition_around_array(input_array, i, right)

  partition_around_array(input_array, 0, len(input_array) - 1)

  global global_count
  count = global_count
  global_count = 0
  return count 


def select_first(left, right):
  return left
 

def select_last(left, right):
  return right


def select_middle(input_array, left, right):
  middle = left + ((right - left) // 2)
  median = statistics.median([input_array[left], input_array[right], input_array[middle]])
  middle_index = input_array.index(median)
  return middle_index


def main():
  data = sys.stdin.read()
  data_set1 = list(map(int, data.split()))
  data_set2 = copy.copy(data_set1)
  data_set3 = copy.copy(data_set1)
  print(count_sort(data_set1, 'left'))
  print(count_sort(data_set2, 'right'))
  print(count_sort(data_set3, 'middle'))

if __name__ == '__main__':
  main()