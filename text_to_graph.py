from pprint import pprint

# first get all lines from file
with open('', 'r') as f:
    lines = f.readlines()

# make the graph from file
graph = {}
for line in lines:
    newline = line.split()
    for i in range(len(newline)):
        num = int(newline[i])
        newline[i] = num

    graph[newline[0]] = newline[1:]

graph = str(graph)

# finally, write lines in the file
with open('', 'w') as f:
    f.writelines(graph)