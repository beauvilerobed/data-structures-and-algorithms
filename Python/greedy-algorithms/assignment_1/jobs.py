from heapq import heappop, heappush
import sys

def scheduling(jobs):
    job_array = []
    job_heap = []
    for job_pair in jobs:
        weight = job_pair[0]
        length = job_pair[1]
        difference = weight - length
        heappush(job_heap, [-1 * difference, -1 * weight, -1 * length])
    
    for _ in range(len(job_heap)):
        value = heappop(job_heap)
        job_array.append([-1 * value[0], -1 * value[1], -1 * value[2]])
    
    total = 0
    completion_time = 0

    for _, weight, length in job_array:
        completion_time += length
        total += weight * completion_time
    
    return total

def scheduling_ratio(jobs):
    job_array = []
    job_heap = []
    for job_pair in jobs:
        weight = job_pair[0]
        length = job_pair[1]
        ratio = weight / length
        heappush(job_heap, [-1 * ratio, -1 * weight, -1 * length])
    
    for _ in range(len(job_heap)):
        value = heappop(job_heap)
        job_array.append([-1 * value[0], -1 * value[1], -1 * value[2]])
    
    total = 0
    completion_time = 0

    for _, weight, length in job_array:
        completion_time += length
        total += weight * completion_time
    
    return total

def main():
    data = sys.stdin.read()
    data_set = data.split()
    case = []
    for values in data_set[1:]:
        weight, length = list(map(int, values.split()))
        case.append([weight, length])
    
    print(scheduling(case))
    print(scheduling_ratio(case))

if __name__ == '__main__':
    main()