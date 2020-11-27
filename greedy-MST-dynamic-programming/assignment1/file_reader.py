import os
import glob
import heapq


def generate_files(path='/tests/*'):
    file_path = os.getcwd() + path
    len_file = len(file_path) - 1

    paths = glob.glob(file_path)
    input_files = []
    output_files = []

    for path in paths:
        if path[len_file: len_file + 5] == 'input':
            input_files.append(path)
        elif path[len_file: len_file + 6] == 'output':
            output_files.append(path)

    input_files.sort()
    output_files.sort()

    return input_files, output_files


def generate_cases_prim(input_files, output_files):

    temp = generate_temp_cases(input_files, output_files)

    cases = []
    for input_output in temp:
        case = input_output[0]
        data = input_output[1]
        graph = {}
        for value in case[1:]:
            vertex = value[0]
            edge = value[1]
            edge_value = value[2]
            if vertex in graph:
                heapq.heappush(graph[vertex], [edge_value, edge])
            else:
                graph[vertex] = []
                heapq.heappush(graph[vertex], [edge_value, edge])

            if edge != vertex:
                if edge in graph:
                    heapq.heappush(graph[edge], [edge_value, vertex])
                else:
                    graph[edge] = []
                    heapq.heappush(graph[edge], [edge_value, vertex])
        cases.append([graph, data])

    return cases


def generate_temp_cases(input_files, output_files):
    temp = []
    for name1, name2 in zip(input_files, output_files):
        case = []
        with open(name1, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = list(map(int, line.split()))
                case.append(data)
        with open(name2, 'r') as f:
            line = f.readline()
            data = int(line)

        temp.append([case, data])
    return temp


def generate_cases_jobs(input_files, output_files):
    cases = []
    for name1, name2 in zip(input_files, output_files):
        case = []
        with open(name1, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                weight, length = list(map(int, line.split()))
                case.append([weight, length])
        with open(name2, 'r') as f:
            lines = f.readlines()
            data = list(map(int, lines))

        cases.append([case, data])

    return cases
