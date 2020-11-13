# python3

# Parallel processing

# Task. You have a program which is parallelized and uses 𝑛 
# independent threads to process the given list of 𝑚 jobs. 
# Threads take jobs in the order they are given in the input. 
# If there is a free thread, it immediately takes the next job 
# from the list. If a thread has started processing a job, it 
# doesn’t interrupt or stop until it finishes processing the 
# job. If several threads try to take jobs from the list 
# simultaneously, the thread with smaller index takes the job. 
# For each job you know exactly how long will it take any thread 
# to process this job, and this time is the same for all the 
# threads. You need to determine for each job which thread will 
# process it and when will it start processing.

from collections import namedtuple
from queue import PriorityQueue

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs_naive(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def assign_jobs(n_workers, jobs):

    len_jobs = len(jobs)
    tasks = []
    job_queue = PriorityQueue()

    if n_workers >= len_jobs:
        for i in range(len_jobs):
            tasks.append(AssignedJob(i, 0))

    else:
        for i in range(n_workers):
            job_queue.put([jobs[i], i])
            tasks.append(AssignedJob(i, 0))
    
        for i in range(n_workers, len_jobs):
            temp = job_queue.get()
            time = temp[0]
            thread_name = temp[1]
            tasks.append(AssignedJob(thread_name, time))
            job_queue.put([time+jobs[i], thread_name])
        
    return tasks


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
